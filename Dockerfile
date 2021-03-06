FROM python:3.9-slim

COPY . ./

RUN pip install Flask flask-restful gunicorn numpy

CMD exec gunicorn --bind :80 app:app