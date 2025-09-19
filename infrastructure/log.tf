resource "aws_cloudwatch_log_group" "tiny_kraken_hydration_reminder" {
  name              = "/aws/lambda/tiny-kraken-hydration-reminder"
  retention_in_days = 3
  tags              = var.common_tags
}

resource "aws_cloudwatch_log_group" "tiny_kraken_api" {
  name              = "/aws/lambda/tiny-kraken-api"
  retention_in_days = 3
  tags              = var.common_tags
}
