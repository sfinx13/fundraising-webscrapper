#syntax=docker/dockerfile:1

FROM python:3.11.0rc1-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]