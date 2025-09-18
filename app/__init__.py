# app/__init__.py
from flask import Flask
from .config import Config
from .extensions import db

def create_app(config_object=Config):
    """
    Application factory. Inicializa Flask, extensiones y blueprints.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)

    # Inicializar extensiones
    db.init_app(app)

    # Aquí podrías registrar blueprints, comandos, etc.
    from .views import  main_bp
    app.register_blueprint(main_bp)

    return app

