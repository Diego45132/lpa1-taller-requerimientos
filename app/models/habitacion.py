from datetime import datetime
from app.extensions import db

class Habitacion(db.Model):
    """
    Modelo Habitacion.
    Contiene métodos de negocio como comprobar disponibilidad y calcular precio final.
    """
    __tablename__ = 'habitaciones'

    id = db.Column(db.Integer, primary_key=True)
    hotel_id = db.Column(db.Integer, db.ForeignKey('hoteles.id'), nullable=False)
    tipo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    precio_base = db.Column(db.Float, nullable=False, default=0.0)
    capacidad = db.Column(db.Integer, nullable=False, default=1)
    activa = db.Column(db.Boolean, default=True)
    servicios_incluidos = db.Column(db.Text)  # JSON o CSV si se desea
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    reservas = db.relationship('Reserva', backref='habitacion', lazy='dynamic', cascade="all, delete-orphan")
    calificaciones = db.relationship('Calificacion', backref='habitacion', lazy='dynamic', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Habitacion {self.tipo} - Hotel {self.hotel_id}>"

    @classmethod
    def create(cls, hotel, tipo, precio_base, capacidad, **kwargs):
        """Crea una habitación y la asocia a un hotel."""
        hab = cls(hotel=hotel, tipo=tipo, precio_base=precio_base, capacidad=capacidad, **kwargs)
        db.session.add(hab)
        db.session.commit()
        return hab

    def set_active(self, active: bool):
        """Activa o desactiva la habitación (ej. mantenimiento)."""
        self.activa = active
        db.session.commit()

    def is_available(self, start_date, end_date):
        """
        Verifica disponibilidad: devuelve True si no existen reservas confirmadas
        que se crucen con el rango [start_date, end_date).
        """
        overlapping = self.reservas.filter(
            Reserva.estado == 'confirmada',
            Reserva.fecha_inicio < end_date,
            Reserva.fecha_fin > start_date
        ).count()
        return overlapping == 0 and self.activa and self.hotel.activo

    def average_rating(self):
        """Calcula la calificación promedio de la habitación."""
        total = 0
        count = 0
        for c in self.calificaciones:
            total += c.puntaje
            count += 1
        return (total / count) if count else None

    def calculate_price(self, start_date, end_date, guests=1, temporada=None, promocion=None):
        """
        Calcula el precio total por estancia teniendo en cuenta:
         - precio_base,
         - multiplicador por número de huéspedes si aplica,
         - temporada (si se define, puede ajustar precio),
         - promoción (aplica descuento porcentual).
        Retorna (precio_total, breakdown_dict).
        """
        nights = (end_date - start_date).days
        base = self.precio_base * nights

        # Ajuste por huéspedes (si excede capacidad => error en caller)
        extra_guest_multiplier = 1.0
        if guests > self.capacidad:
            raise ValueError("Número de huéspedes excede la capacidad de la habitación")

        # aplica temporada: supongamos temporada tiene atributo factor_precio (1.0 por defecto)
        temporada_factor = getattr(temporada, 'factor_precio', 1.0) if temporada else 1.0
        precio_temporada = base * temporada_factor

        descuento = 0.0
        if promocion:
            descuento = precio_temporada * (promocion.descuento / 100.0)

        total = precio_temporada - descuento

        breakdown = {
            "nights": nights,
            "precio_base": base,
            "temporada_factor": temporada_factor,
            "precio_con_temporada": precio_temporada,
            "descuento": descuento,
            "total": total
        }
        return total, breakdown

    def to_dict(self):
        return {
            "id": self.id,
            "hotel_id": self.hotel_id,
            "tipo": self.tipo,
            "precio_base": self.precio_base,
            "capacidad": self.capacidad,
            "activa": self.activa
        }

# Import circular resolver: Reserva y Calificacion referenciadas en método is_available/relationships
from .reserva import Reserva  # noqa: E402,F401
from .calificacion import Calificacion  # noqa: E402,F401
