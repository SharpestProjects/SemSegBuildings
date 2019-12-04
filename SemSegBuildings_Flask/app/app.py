#import rastervision as rv
import os 
from flask import Flask, request


# s3 uri
#s3 = os.environ['$S3_BACKEND']
# load up prediction package and tmp working directory
#p = Predictor(s3, '/tmp')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def run():
    if request.method == 'GET':
        return 'test'

if __name__ == '__main__':
    app.run()

