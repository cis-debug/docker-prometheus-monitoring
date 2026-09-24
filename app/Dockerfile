# Image Python légère
FROM python:3.12-slim

# Dossier de travail dans le conteneur
WORKDIR /app

# Installer dépendances d'abord (cache Docker)
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copier le code
COPY app.py /app/app.py

# Port interne
EXPOSE 5000

# Lancer l'app
CMD ["python", "/app/app.py"]
