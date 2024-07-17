# Usar la imagen oficial de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Instalar ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

# Copiar el archivo de requerimientos
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . .

# Ejecutar el script

CMD ["./run_all.sh"]