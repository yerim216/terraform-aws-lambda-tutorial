resource "aws_dynamodb_table" "users_table" {
  name         = "Users"
  billing_mode = "PAY_PER_REQUEST"

  attribute {
    name = "id"
    type = "S"
  }

  attribute {
    name = "name"
    type = "S"
  }

  hash_key  = "id"
  range_key = "name"

  global_secondary_index {
    name            = "NicknameIndex"
    hash_key        = "nickName"
    projection_type = "ALL"

    attribute {
      name = "nickName"
      type = "S"
    }
  }

  global_secondary_index {
    name            = "AgeIndex"
    hash_key        = "age"
    projection_type = "ALL"

    attribute {
      name = "age"
      type = "N"
    }
  }
}
