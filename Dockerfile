FROM python:3.11.9-bookworm

WORKDIR /app
COPY src src
COPY data data
COPY requirements.txt ./
COPY .env ./

RUN pip install -r requirements.txt

CMD ["fastapi","run","src/app.py"]

EXPOSE 8000
