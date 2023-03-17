FROM python:3.9-slim-buster

# Crea y establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requisitos a la imagen y, a continuación, instala las dependencias
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación en la imagen
COPY . .

# Establece la variable de entorno FLASK_APP y FLASK_ENV
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Expone el puerto 5000 para que pueda ser accesible desde fuera del contenedor
EXPOSE 5000

# Arranca la aplicación
CMD ["flask", "run", "--host=0.0.0.0"]
