resource "aws_dynamodb_table" "tiny_kraken_db" {
  name           = "tiny-kraken-db"
  hash_key       = "pk"
  range_key      = "sk"
  read_capacity  = 5
  write_capacity = 5
  attribute {
    name = "pk"
    type = "S"
  }
  attribute {
    name = "sk"
    type = "S"
  }
  attribute {
    name = "created_at"
    type = "S"
  }

  tags = var.common_tags

  global_secondary_index {
    name            = "TinyKrakenGlobalSecondaryIndex"
    hash_key        = "pk"
    range_key       = "created_at"
    projection_type = "ALL"
    read_capacity   = 5
    write_capacity  = 5
  }
}
