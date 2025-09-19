data "archive_file" "tiny_kraken_hydration_reminder_file" {
  type        = "zip"
  source_dir  = "${path.module}/../services"
  output_path = "${path.module}/../tiny_kraken_hydration_reminder.zip"
  excludes    = ["tests", "api"]
}

data "archive_file" "tiny_kraken_api_file" {
  type        = "zip"
  source_dir  = "${path.module}/../services"
  output_path = "${path.module}/../tiny_kraken_api.zip"
  excludes    = ["tests", "hydration_reminder"]
}

resource "aws_lambda_function" "tiny_kraken_hydration_reminder" {
  function_name    = "tiny-kraken-hydration-reminder"
  handler          = "hydration_reminder.handler.lambda_handler"
  runtime          = "python3.11"
  filename         = data.archive_file.tiny_kraken_hydration_reminder_file.output_path
  source_code_hash = data.archive_file.tiny_kraken_hydration_reminder_file.output_base64sha256
  role             = aws_iam_role.lambda_exec.arn
  tags             = merge(var.common_tags, { Service = "HydrationReminder" })
  timeout          = 30
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
    log_group  = aws_cloudwatch_log_group.tiny_kraken_hydration_reminder.name
  }
}

resource "aws_lambda_function" "tiny_kraken_api" {
  function_name    = "tiny-kraken-api"
  handler          = "api.handler.lambda_handler"
  runtime          = "python3.11"
  filename         = data.archive_file.tiny_kraken_api_file.output_path
  source_code_hash = data.archive_file.tiny_kraken_api_file.output_base64sha256
  role             = aws_iam_role.lambda_exec.arn
  tags             = merge(var.common_tags, { Service = "API" })
  timeout          = 30


  logging_config {
    log_format = "Text"
    log_group  = aws_cloudwatch_log_group.tiny_kraken_api.name
  }
}
