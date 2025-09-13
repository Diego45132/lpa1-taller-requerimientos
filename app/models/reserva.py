# app/models/reserva.py
from datetime import datetime
from app.extensions import db

class Reserva(db.Model):
    """
    Reserva de habitación por un cliente.
    Estados: pendiente, confirmada, cancelada
    """
    __tablename__ = 'reservas'

    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    habitacion_id = db.Column(db.Integer, db.ForeignKey('habitaciones.id'), nullable=False)
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_fin = db.Column(db.Date, nullable=False)
    estado = db.Column(db.String(50), default='pendiente')  # pendiente, confirmada, cancelada
    monto_total = db.Column(db.Float, default=0.0)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

    pago = db.relationship('Pago', uselist=False, backref='reserva', cascade="all, delete-orphan")
    calificaciones = db.relationship('Calificacion', backref='reserva', lazy='dynamic', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Reserva {self.id} cliente {self.cliente_id} habitacion {self.habitacion_id}>"

    @classmethod
    def create(cls, cliente, habitacion, fecha_inicio, fecha_fin, monto_total, estado='pendiente'):
        """
        Crea una reserva (sin procesar pago).
        El caller debe validar disponibilidad antes de invocar.
        """
        reserva = cls(
            cliente_id=cliente.id,
            habitacion_id=habitacion.id,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            monto_total=monto_total,
            estado=estado
        )
        db.session.add(reserva)
        db.session.commit()
        return reserva

    def confirm(self):
        """Confirma una reserva (normalmente luego de pago exitoso)."""
        self.estado = 'confirmada'
        db.session.commit()

    def cancel(self, motivo=None):
        """Cancela la reserva y aplica lógica de reembolso en caller o en Pago."""
        self.estado = 'cancelada'
        db.session.commit()

    def overlaps(self, start_date, end_date):
        """Retorna True si la reserva se superpone con [start_date, end_date)."""
        return self.fecha_inicio < end_date and self.fecha_fin > start_date

    def to_dict(self):
        return {
            "id": self.id,
            "cliente_id": self.cliente_id,
            "habitacion_id": self.habitacion_id,
            "fecha_inicio": str(self.fecha_inicio),
            "fecha_fin": str(self.fecha_fin),
            "estado": self.estado,
            "monto_total": self.monto_total
        }
