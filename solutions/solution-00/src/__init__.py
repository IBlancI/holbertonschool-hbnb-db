""" Initialisation de l'application Flask. """

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

# Initialisation des extensions
cors = CORS()
db = SQLAlchemy()
jwt = JWTManager()
bcrypt = Bcrypt()

def create_app(config_class="src.config.DevelopmentConfig") -> Flask:
    """
    Crée une application Flask avec la classe de configuration donnée.
    La classe de configuration par défaut est DevelopmentConfig.
    """
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
    app.config['JWT_SECRET_KEY'] = 'hbnb im tired'
    app.url_map.strict_slashes = False

    app.config.from_object(config_class)

    register_extensions(app)
    register_routes(app)
    register_handlers(app)

    return app

def register_extensions(app: Flask) -> None:
    """Enregistre les extensions pour l'application Flask"""
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})
    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

def register_routes(app: Flask) -> None:
    """Importe et enregistre les routes pour l'application Flask"""
    
    from src.routes.users import users_bp
    from src.routes.countries import countries_bp
    from src.routes.cities import cities_bp
    from src.routes.places import places_bp
    from src.routes.amenities import amenities_bp
    from src.routes.reviews import reviews_bp

    app.register_blueprint(users_bp)
    app.register_blueprint(countries_bp)
    app.register_blueprint(cities_bp)
    app.register_blueprint(places_bp)
    app.register_blueprint(amenities_bp)
    app.register_blueprint(reviews_bp)

def register_handlers(app: Flask) -> None:
    """Enregistre les gestionnaires d'erreurs pour l'application Flask."""
    app.errorhandler(404)(lambda e: ({"error": "Not found", "message": str(e)}, 404))
    app.errorhandler(400)(lambda e: ({"error": "Bad request", "message": str(e)}, 400))
