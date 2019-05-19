import os
import boto3

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
AWS_DYNAMODB_ENDPOINT = os.environ.get('AWS_DYNAMODB_ENDPOINT', '')
AWS_REGION_NAME = os.environ.get('AWS_REGION_NAME', '')

dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION_NAME, endpoint_url=AWS_DYNAMODB_ENDPOINT)

table = dynamodb.Table('Personas')

table.delete()

if __name__ == '__main__':
    print('Eliminando tabla')