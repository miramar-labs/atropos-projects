FROM python:3.12-slim

WORKDIR /backend

COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY ./app ./app
COPY ./frontend ./frontend

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]