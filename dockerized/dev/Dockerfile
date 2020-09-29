FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir -p /opt/dev
WORKDIR /opt/dev
COPY dockerized/dev/requirements.txt /opt/dev/
COPY . /opt/cornucopia
RUN pip install -e /opt/cornucopia
RUN pip install -r requirements.txt
COPY dockerized/dev/ /opt/dev/

