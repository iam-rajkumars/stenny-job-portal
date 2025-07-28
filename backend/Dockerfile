FROM python:3.11-slim

WORKDIR /app

COPY backend/ .  # Assuming backend has main.py and requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python", "main.py"]

