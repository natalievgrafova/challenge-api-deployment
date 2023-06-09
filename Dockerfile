FROM python:latest
RUN mkdir /app
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD uvicorn app:app --host 0.0.0.0. --port 8000

