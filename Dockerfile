
FROM python:3


MAINTAINER Felipe

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

ADD requirements.txt /app/

RUN pip install pip -U
RUN pip install -r requirements.txt

ADD . /app/

RUN chmod +x docker-entrypoint.sh
