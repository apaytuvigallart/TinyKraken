resource "aws_cloudwatch_log_group" "this" {
  name              = "/aws/lambda/tiny-kraken"
  retention_in_days = 3
  tags              = var.common_tags
}
