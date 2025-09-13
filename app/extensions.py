# app/extensions.py
from flask_sqlalchemy import SQLAlchemy

# Instancia global de SQLAlchemy para ser inicializada desde la factory
db = SQLAlchemy()
