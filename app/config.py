# app/config.py
import os

class Config:
    """Configuración base para la aplicación Flask."""
    SECRET_KEY = os.environ.get("SECRET_KEY", "cambiame-en-produccion")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///pms.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
