from flask import Flask, request, render_template
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
    list_name = []
    for object in list:
        list_name.append(object)

    return render_template('objects.html', objects=list_name)

@app.route('/download/<object>', methods=['GET'])
def download(object):
    import botocore
    s3 = boto3.resource('s3')
    try:
        s3.Bucket('python-boto301').download_file(object, object)
        return '<h1>Se descargo con exito</h1>'
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == '404':
            return '<h1>El archivo no existe</h1>'
        else:
            return '<h1>Opps<h1>'
    
        
if __name__ == '__main__':
    app.run(debug=True)