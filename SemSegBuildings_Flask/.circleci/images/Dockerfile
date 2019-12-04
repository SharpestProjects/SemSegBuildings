FROM quay.io/azavea/raster-vision:pytorch-latest
COPY ../../app/app.py /opt/app.py
COPY ../../requirements.txt /opt/requirements.txt
RUN pip install -r requirements.txt
RUN python app.py
