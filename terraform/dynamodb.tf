resource "aws_dynamodb_table" "tiny_kraken_db" {
    name = "tiny-kraken-db"
    hash_key = "id"

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
