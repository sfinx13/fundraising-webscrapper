#syntax=docker/dockerfile:1

FROM python:3.13.0a3-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]