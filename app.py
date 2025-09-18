# TODO: desarrollar el sistema
from app import create_app
from app.extensions import db

app = create_app()

if __name__ == '__main__':
    # Crear tablas en SQLite para desarrollo rápido; en producción usar migraciones.
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0')
