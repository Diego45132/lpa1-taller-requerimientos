from datetime import datetime
from app.extensions import db

class Hotel(db.Model):
    """
    Representa un hotel.
    """
    __tablename__ = 'hoteles'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    direccion = db.Column(db.String(512), nullable=False)
    telefono = db.Column(db.String(50))
    email = db.Column(db.String(255))
    ubicacion = db.Column(db.String(255))  # Puede ser ciudad/país o coordenadas
    descripcion_servicios = db.Column(db.Text)
    activo = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relaciones
    habitaciones = db.relationship('Habitacion', backref='hotel', lazy='dynamic', cascade="all, delete-orphan")
    promociones = db.relationship('Promocion', backref='hotel', lazy='dynamic', cascade="all, delete-orphan")
    temporadas = db.relationship('Temporada', backref='hotel', lazy='dynamic', cascade="all, delete-orphan")
    politica_pago = db.relationship('PoliticaPago', uselist=False, backref='hotel', cascade="all, delete-orphan")
    politica_cancelacion = db.relationship('PoliticaCancelacion', uselist=False, backref='hotel', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Hotel {self.nombre}>"

    @classmethod
    def create(cls, **kwargs):
        """Crea y persiste un hotel."""
        hotel = cls(**kwargs)
        db.session.add(hotel)
        db.session.commit()
        return hotel

    def update(self, **kwargs):
        """Actualiza campos del hotel y persiste."""
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)
        db.session.commit()
        return self

    def deactivate(self):
        """Marca el hotel como inactivo (no acepta reservas)."""
        self.activo = False
        db.session.commit()

    def activate(self):
        """Marca el hotel como activo."""
        self.activo = True
        db.session.commit()

    def to_dict(self):
        """Representación serializable mínima del hotel."""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "direccion": self.direccion,
            "telefono": self.telefono,
            "email": self.email,
            "ubicacion": self.ubicacion,
            "activo": self.activo,
        }
