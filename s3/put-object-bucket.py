from flask import Flask, request
import boto3

app = Flask(__name__)

@app.route('/')
def index():
    return '''<form method=POST enctype=multipart/form-data action="upload">
        <input type=file name=myfile>
        <input type=submit>
        </form>'''

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['myfile']
    name_file = file.filename
    s3 = boto3.resource('s3')
    s3.Bucket('python-boto301').put_object(Key=name_file, Body=file)
    return '<h1>File saved to S3</h1>'
    
@app.route('/get-objects', methods=['GET'])
def get_objects():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('python-boto301')
    list = bucket.objects.all()
    for object in list:
        print(object)
    return '<h1>Cargando los objetos</h1>'

if __name__ == '__main__':
    app.run(debug=True)