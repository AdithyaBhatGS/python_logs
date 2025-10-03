FROM python:3.11-slim

WORKDIR /app

RUN mkdir logs

COPY . /app

CMD ["python", "run.py"]

