FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app

WORKDIR /app

COPY application/ /app
COPY ./requirements.txt /app

RUN pip install -r requirements.txt

EXPOSE 80

ENV NAME wordcount

RUN python manage.py collectstatic