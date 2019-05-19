import boto3
import json
import decimal

import os

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
AWS_DYNAMODB_ENDPOINT = os.environ.get('AWS_DYNAMODB_ENDPOINT', '')
AWS_REGION_NAME = os.environ.get('AWS_REGION_NAME', '')

dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION_NAME, endpoint_url=AWS_DYNAMODB_ENDPOINT)

table = dynamodb.Table('Personas')

with open("dynamodb/personas.json") as json_file:
    personas = json.load(json_file, parse_float = decimal.Decimal)
    for person in personas:
        id = str(person['id'])
        nombre = person['nombre']
        edad = person['edad']

        table.put_item(
            Item={
                'id': id,
                'nombre': nombre,
                'edad': edad
            }
        )

if __name__ == '__main__':
    print('Cargando datos')