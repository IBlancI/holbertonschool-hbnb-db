# app/initialize_db.py
import os
from app import db

def initialize_database(app):
    if app.config['ENV'] == 'development':
        if not os.path.exists('dev.db'):
            db.create_all()

initialize_database(db.get_app())
