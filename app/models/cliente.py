# app/models/cliente.py
from datetime import datetime
from app.extensions import db

class Cliente(db.Model):
    """
    Representa un cliente/huésped registrado en el sistema.
    """
    __tablename__ = 'clientes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    telefono = db.Column(db.String(50))
    direccion = db.Column(db.String(512))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    reservas = db.relationship('Reserva', backref='cliente', lazy='dynamic', cascade="all, delete-orphan")
    calificaciones = db.relationship('Calificacion', backref='cliente', lazy='dynamic', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Cliente {self.email}>"

    @classmethod
    def create(cls, nombre, email, telefono=None, direccion=None):
        """Crea un cliente y persiste en BD."""
        cliente = cls(nombre=nombre, email=email, telefono=telefono, direccion=direccion)
        db.session.add(cliente)
        db.session.commit()
        return cliente

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email,
            "telefono": self.telefono,
        }
