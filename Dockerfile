# syntax=docker/dockerfile:1
FROM python:slim-buster
WORKDIR /usr/src/app
COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .