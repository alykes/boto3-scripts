import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('customers')

def lambda_handler(event, context):
    response = table.get_item(
       Key={
           'id': 'alykes'
       }
    )
    print(response)

    return {
    'StausCodet': 200,
    'body': response
    }
