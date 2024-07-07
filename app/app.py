from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Importer les modèles ici pour éviter les références circulaires
from models import User

# Initialisation de la base de données
with app.app_context():
    db.create_all()

# Ajouter des routes et des blueprints ici

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
