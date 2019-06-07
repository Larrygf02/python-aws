import boto3

#s3 = boto3.resource('s3')

client = boto3.client('s3')

#El nombre del bucket debe ser unico y que no exista
#en ninguna region
response = client.create_bucket(
    Bucket='python-boto301',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-2'
    })

print(response)
