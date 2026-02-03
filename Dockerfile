# Usar una imagen ligera de Python
FROM python:3.11-slim

# Instalar dependencias necesarias para kafka-python y utilidades
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos de dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Por defecto no ejecuta nada, se define en docker-compose
CMD ["python"]
