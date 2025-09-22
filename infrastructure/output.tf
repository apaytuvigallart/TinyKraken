output "api_gateway_url" {
  description = "Invoke URL for the API Gateway"
  value       = aws_api_gateway_stage.prod.invoke_url
}
