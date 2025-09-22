data "aws_region" "current" {}
data "aws_caller_identity" "current" {}

# API Gateway for TinyKraken service
resource "aws_api_gateway_rest_api" "tinykraken_api" {
  name        = "tinykraken-api"
  description = "API Gateway for TinyKraken service"
  tags        = var.common_tags
  endpoint_configuration {
    types = ["REGIONAL"]
  }
}

# Resources for the API Gateway
resource "aws_api_gateway_resource" "comments" {
  rest_api_id = aws_api_gateway_rest_api.tinykraken_api.id
  parent_id   = aws_api_gateway_rest_api.tinykraken_api.root_resource_id
  path_part   = "comments"
}

resource "aws_api_gateway_resource" "comment_id" {
  rest_api_id = aws_api_gateway_rest_api.tinykraken_api.id
  parent_id   = aws_api_gateway_resource.comments.id
  path_part   = "{comment_id}"
}

# Methods for the API Gateway
resource "aws_api_gateway_method" "list_comments" {
  rest_api_id   = aws_api_gateway_rest_api.tinykraken_api.id
  resource_id   = aws_api_gateway_resource.comments.id
  http_method   = "GET"
  authorization = "NONE"
}

resource "aws_api_gateway_method" "get_comment_id" {
  rest_api_id   = aws_api_gateway_rest_api.tinykraken_api.id
  resource_id   = aws_api_gateway_resource.comment_id.id
  http_method   = "GET"
  authorization = "NONE"
}

# Integrations for the API Gateway resources
resource "aws_api_gateway_integration" "comments_integration" {
  rest_api_id = aws_api_gateway_rest_api.tinykraken_api.id
  resource_id = aws_api_gateway_resource.comments.id
  http_method = aws_api_gateway_method.list_comments.http_method
  uri         = aws_lambda_function.tiny_kraken_api.invoke_arn
  type        = "AWS_PROXY"

  # Lambda function can only be invoked with POST method, see https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/api_gateway_integration#integration_http_method-1
  integration_http_method = "POST"
}

resource "aws_api_gateway_integration" "comment_integration" {
  rest_api_id             = aws_api_gateway_rest_api.tinykraken_api.id
  resource_id             = aws_api_gateway_resource.comment_id.id
  http_method             = aws_api_gateway_method.get_comment_id.http_method
  uri                     = aws_lambda_function.tiny_kraken_api.invoke_arn
  type                    = "AWS_PROXY"
  integration_http_method = "POST"
}

# Deployments for the API Gateway
resource "aws_api_gateway_deployment" "tinykraken_deployment" {
  rest_api_id = aws_api_gateway_rest_api.tinykraken_api.id

  depends_on = [
    aws_api_gateway_integration.comments_integration,
    aws_api_gateway_integration.comment_integration,
  ]
}

# Stages for the API Gateway
resource "aws_api_gateway_stage" "prod" {
  stage_name    = "prod"
  rest_api_id   = aws_api_gateway_rest_api.tinykraken_api.id
  deployment_id = aws_api_gateway_deployment.tinykraken_deployment.id
}

# Permissions for API Gateway to invoke the Lambda function
resource "aws_lambda_permission" "apigw_lambda" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.tiny_kraken_api.function_name
  principal     = "apigateway.amazonaws.com"

  # More: http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-control-access-using-iam-policies-to-invoke-api.html
  source_arn = "arn:aws:execute-api:${data.aws_region.current.region}:${data.aws_caller_identity.current.account_id}:${aws_api_gateway_rest_api.tinykraken_api.id}/*/*"
}
