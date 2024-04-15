
FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# Comando para ejecutar aplicación Flask cuando el contenedor se inicie
CMD ["python", "app.py"]
