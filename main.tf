module "lambda" {
  source = "./modules/lambda"
}

module "api_gateway" {
  source = "./modules/api_gateway"
}

module "dynamodb" {
  source = "./modules/dynamodb"
}
