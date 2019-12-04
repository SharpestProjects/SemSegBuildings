import rastervision as rv
import os 


# s3 uri
s3 = os.environ['$S3_BACKEND']
# load up prediction package and tmp working directory
p = Predictor(s3, '/tmp')

app = Flask(__app__)


