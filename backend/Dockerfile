# ✅ Base image with Python
FROM python:3.11-slim

# ✅ Set working directory
WORKDIR /app

# ✅ Copy dependencies and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Copy your backend code
COPY . .

# ✅ Run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

