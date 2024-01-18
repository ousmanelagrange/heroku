# Utilisation de l'image officielle de Python comme point de départ
FROM python:3.9

# Définition du repertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur

COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code source dans le conteneur
COPY . .

# Exposer le port sur lequel le server Django fonctionne
EXPOSE 8000

# Commande pour démarrer le server django
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]
