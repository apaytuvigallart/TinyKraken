resource "aws_dynamodb_table" "tiny_kraken_db" {
  name           = "tiny-kraken-db"
  hash_key       = "id"
  read_capacity  = 5
  write_capacity = 5
  attribute {
    name = "id"
    type = "S"
  }
  attribute {
    name = "text"
    type = "S"
  }
  attribute {
    name = "created_at"
    type = "S"
  }
  tags = var.common_tags
}
