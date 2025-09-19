from app import create_app
from app.extensions import db
from app.models import Hotel, Habitacion

app = create_app()

with app.app_context():
    # Crear hotel de ejemplo si no existe
    hotel = Hotel.query.filter_by(nombre="Hotel Ejemplo").first()
    if not hotel:
        hotel = Hotel(nombre="Hotel Ejemplo", direccion="Calle Falsa 123", telefono="123456789", email="ejemplo@hotel.com", ubicacion="Ciudad Ejemplo", descripcion_servicios="WiFi, Piscina, Desayuno")
        db.session.add(hotel)
        db.session.commit()
        print("Hotel de ejemplo creado.")
    else:
        print("Hotel de ejemplo ya existe.")

    # Crear habitaciones de ejemplo si no existen
    if Habitacion.query.filter_by(hotel_id=hotel.id).count() == 0:
        habitaciones = [
            Habitacion(hotel_id=hotel.id, tipo="Simple", descripcion="Habitación simple", precio_base=50.0, capacidad=1, activa=True, imagen="madrid.png"),
            Habitacion(hotel_id=hotel.id, tipo="Doble", descripcion="Habitación doble", precio_base=80.0, capacidad=2, activa=True, imagen="paris.png"),
            Habitacion(hotel_id=hotel.id, tipo="Suite", descripcion="Suite de lujo", precio_base=150.0, capacidad=4, activa=True, imagen="tokio.png"),
            Habitacion(hotel_id=hotel.id, tipo="MegaSuite", descripcion="presidencial", precio_base=350.0, capacidad=4, activa=True, imagen="miami.png")
        ]
        db.session.add_all(habitaciones)
        db.session.commit()
        print("Habitaciones de ejemplo creadas.")
    else:
        print("Las habitaciones de ejemplo ya existen.")
