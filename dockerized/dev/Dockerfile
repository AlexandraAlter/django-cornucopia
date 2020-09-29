FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir -p /opt/dev
WORKDIR /opt/dev
COPY requirements.txt /opt/dev/
RUN pip install -r requirements.txt
COPY . /opt/dev/

