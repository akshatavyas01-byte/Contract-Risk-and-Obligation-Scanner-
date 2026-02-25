FROM python:3.10-slim

WORKDIR /app

COPY  . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

EXPOSE 8051

CMD [ "bash","start.sh" ]