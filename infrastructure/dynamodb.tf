resource "aws_dynamodb_table" "tiny_kraken_db" {
  name           = "tiny-kraken-db"
  hash_key       = "pk"
  range_key      = "comment_id"
  read_capacity  = 5
  write_capacity = 5
  attribute {
    name = "pk"
    type = "S"
  }
  attribute {
    name = "comment_id"
    type = "S"
  }
  attribute {
    name = "created_at"
    type = "S"
  }

  global_secondary_index {
    name            = "TinyKrakenEntryIndex"
    hash_key        = "pk"
    range_key       = "created_at"
    read_capacity   = 5
    write_capacity  = 5
    projection_type = "ALL"
  }

  tags = var.common_tags

}
