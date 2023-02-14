# syntax=docker/dockerfile:1

FROM python:3.10.8-slim-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt-get update

RUN apt-get -y install default-libmysqlclient-dev

RUN apt-get -y install gcc

RUN pip install --upgrade pip

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3","mysite/manage.py", "runserver", "0.0.0.0:8000"]

