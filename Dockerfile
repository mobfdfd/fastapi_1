FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN pip install --upgrade h11 uvicorn fastapi

RUN apt-get update && apt-get install -y tesseract-ocr

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
