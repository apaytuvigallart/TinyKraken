resource "aws_iam_role" "lambda_exec" {
  name = "lambda_exec_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Principal = {
          Service = "lambda.amazonaws.com"
        },
        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_basic_execution" {
  role       = aws_iam_role.lambda_exec.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

data "archive_file" "this" {
  type        = "zip"
  source_dir  = "${path.module}/../hydration_reminder"
  output_path = "${path.module}/../tiny_kraken.zip"
  excludes    = ["${path.module}/../hydration_reminder/tests", "${path.module}/../hydration_reminder/__pycache__"]
}

resource "aws_lambda_function" "tiny_kraken" {
  function_name    = "tiny-kraken"
  handler          = "lambda_function.lambda_handler"
  runtime          = "python3.11"
  filename         = data.archive_file.this.output_path
  source_code_hash = data.archive_file.this.output_base64sha256
  role             = aws_iam_role.lambda_exec.arn

  environment {
    variables = {
      TWILIO_ACCOUNT_SID  = var.twilio_account_sid
      TWILIO_AUTH_TOKEN   = var.twilio_auth_token
      TWILIO_PHONE_NUMBER = var.twilio_phone_number
      TO_PHONE_NUMBER     = var.to_phone_number
      GOOGLE_API_KEY      = var.google_api_key
      GOOGLE_API_URL      = var.google_api_url
    }
  }
  logging_config {
    log_format = "Text"
    log_group  = aws_cloudwatch_log_group.this.name
  }

  tags = var.common_tags

  timeout = 30
}
