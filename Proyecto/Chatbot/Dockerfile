FROM python:3.6
RUN apt-get update && apt-get install sqlite3
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt && python -m spacy download en
WORKDIR /usr/src/app/bot
CMD python sample.py
#COPY app/ .
