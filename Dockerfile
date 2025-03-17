# Imagen base con Python
FROM python:3.9

# Definir el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivos al contenedor
COPY requirements.txt .
COPY iris_nn.py .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar el script
CMD ["python", "iris_nn.py"]
