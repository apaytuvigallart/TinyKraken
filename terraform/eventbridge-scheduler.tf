
resource "aws_scheduler_schedule" "cron" {
  name        = "tiny-kraken-cron"
  description = "Cron schedule for TinyKraken Lambda function"
  flexible_time_window {
    mode = "OFF"
  }
  schedule_expression = "cron(0 14 * * 1-5)" # Every weekday at 14 PM UTC

  target {
    arn      = aws_lambda_function.tiny_kraken.arn
    role_arn = aws_iam_role.lambda_exec.arn
  }
}

resource "aws_lambda_permission" "allow_eventbridge" {
  statement_id  = "AllowExecutionFromEventBridge"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.tiny_kraken.arn
  principal     = "events.amazonaws.com"

  source_arn = aws_scheduler_schedule.cron.arn
}
