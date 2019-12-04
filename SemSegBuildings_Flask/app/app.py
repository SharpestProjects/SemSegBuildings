import rastervision as rv
import os 
from flask import Flask, request


# s3 uri
#s3 = os.environ['$S3_BACKEND']
# load up prediction package and tmp working directory
p = rv.Predictor('./predict_package.zip', '/tmp')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def run():
    if request.method == 'GET':
        return p

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
