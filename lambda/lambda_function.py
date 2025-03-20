import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def lambda_handler(event, context):
    user_id = event.get('queryStringParameters', {}).get('id')
    name = event.get('queryStringParameters', {}).get('name')

    if not user_id or not name:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Missing id or name parameter"})
        }

    try:
        response = table.get_item(
            Key={
                'id': user_id,
                'name': name
            }
        )
       

        item = response.get('Item')

        if not item:
            return {
                "statusCode": 404,
                "body": json.dumps({"message": "User not found"})
            }

        result = {
            "id" : item.get("id"),
            "name" : item.get("name"),
            "nickName" : item.get("nickName"),
            "age" : item.get("age")
        }

        return {
            "statusCode": 200,
            "body": json.dumps(result)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": str(e)})
        }
