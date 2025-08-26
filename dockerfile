# Image de base Python
FROM python:3.9-slim

# Répertoire de travail
WORKDIR /app

# Installation des dépendances système REQUISES pour spaCy
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    && rm -rf /var/lib/apt/lists/*

# Copie des dépendances et installation
COPY requirements.txt .
RUN pip install --no-cache-dir \ 
    --only-binary=:all: \
    -r requirements.txt

# Téléchargement du modèle spaCy
RUN python -m spacy download en_core_web_sm

# Copie du code de l'application
COPY . .

# Exposition du port
EXPOSE 5000

# Commande de démarrage
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]