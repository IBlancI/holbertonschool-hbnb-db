import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///development.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    USE_DATABASE = True  # switch begin true and false 