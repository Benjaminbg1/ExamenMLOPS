# Imagen base oficial
FROM python:3.10

# Evitar prompts interactivos
ENV DEBIAN_FRONTEND=noninteractive

# Establecer directorio de trabajo
WORKDIR /opt/app

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copiar archivos de la app
COPY . .

# Instalar dependencias de Python
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Exponer el puerto esperado por Cloud Run
EXPOSE 5000

# Comando para ejecutar FastAPI con uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]