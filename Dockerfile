FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /code/src
COPY requirements/base.txt /code/src/requirements.txt
WORKDIR /code/src
RUN pip install -r /code/src/requirements.txt

EXPOSE 8000
