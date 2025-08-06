data "archive_file" "this" {
  type        = "zip"
  source_dir  = "${path.module}/../hydration_reminder"
  output_path = "${path.module}/../tiny_kraken.zip"
  excludes    = ["tests", "__pycache__"]
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
