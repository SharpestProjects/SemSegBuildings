import rastervision as rv
import os
from flask_bootstrap import Bootstrap
import folium

#### This needs to be seperated out ####
from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError
from flask_pagedown.fields import PageDownField

class PostForm(FlaskForm):
   body = PageDownField("Select a demo tile", validators=[Required()])
   submit = SubmitField('Submit')
####                                ####


# s3 uri
#s3 = os.environ['$S3_BACKEND']
# load up prediction package and tmp working directory

p = rv.Predictor('./predict_package.zip', '/tmp')

bootstrap = Bootstrap()
app = Flask(__name__)
bootstrap.init_app(app)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        form = PostForm()
        return render_template('index.html', form=form)

@app.route('/map', methods=['GET'])
def map():
    return render_template('map.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
