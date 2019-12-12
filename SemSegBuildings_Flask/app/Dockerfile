FROM quay.io/azavea/raster-vision:pytorch-latest
COPY ./app.py /opt/src/app.py
COPY ./f_requirements.txt /opt/src/f_requirements.txt
COPY ./predict_package.zip /opt/src/predict_package.zip
COPY ./templates/ /opt/src/templates/
WORKDIR /opt/src
RUN pip install -r f_requirements.txt
CMD python app.py
