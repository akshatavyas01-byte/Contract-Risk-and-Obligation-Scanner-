FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    poppler-utils \
    tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*
    
COPY  . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

EXPOSE 8051

CMD [ "bash","start.sh" ]