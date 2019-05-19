import boto3

dynamodb = boto3.resource('dynamodb', region_name=config.AWS_REGION_NAME, endpoint_url=config.AWS_DYNAMODB_ENDPOINT)

table = dynamodb.create_table(
    TableName='Personas',
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'nombre',
            'KeyType': 'RANGE'
        },
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'nombre',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 20,
        'WriteCapacityUnits': 20
    }
)