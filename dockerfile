# Utilisation d'une image Python comme base
FROM python:3.8

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier de dépendances
COPY requirements.txt ./

# Installer les dépendances Python
RUN pip install -r requirements.txt

# Copier le reste des fichiers du projet dans le conteneur
COPY . .

# Commande par défaut pour démarrer l'application (adapter selon votre projet)
CMD ["python", "app.py"]
