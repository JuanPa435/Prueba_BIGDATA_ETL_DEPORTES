FROM python:3.11-slim

# Evitar buffers de Python y archivos .pyc dentro del contenedor
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instalar dependencias del sistema necesarias para paquetes como mysqlclient
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential default-libmysqlclient-dev gcc libffi-dev libssl-dev && \
    rm -rf /var/lib/apt/lists/*

# Copiar dependencias primero para aprovechar la cache de Docker
COPY requirements.txt /app/requirements.txt

# Actualizar pip e instalar requerimientos
RUN python -m pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r /app/requirements.txt

# Copiar el resto del proyecto
COPY . /app

# Comando por defecto
CMD ["python", "Main.py"]
