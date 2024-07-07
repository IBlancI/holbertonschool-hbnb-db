from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Initialisation of database
with app.app_context():
    db.create_all()

# add route here

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
