
resource "aws_scheduler_schedule" "cron" {
  name        = "tiny-kraken-cron"
  description = "Cron schedule for TinyKraken Lambda function"
  flexible_time_window {
    mode = "OFF"
  }
  schedule_expression = "cron(0 10 ? * MON-FRI *)" # Every weekday at 10 AM UTC

  target {
    arn      = aws_lambda_function.tiny_kraken.arn
    role_arn = aws_iam_role.scheduler_role.arn
  }
}
