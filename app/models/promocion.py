from datetime import datetime
from app.extensions import db

class Promocion(db.Model):
    """
    Representa una promoción/oferta de un hotel.
    """
    __tablename__ = 'promociones'

    id = db.Column(db.Integer, primary_key=True)
    hotel_id = db.Column(db.Integer, db.ForeignKey('hoteles.id'), nullable=False)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text)
    descuento = db.Column(db.Float, default=0.0)  # porcentaje
    fecha_inicio = db.Column(db.Date)
    fecha_fin = db.Column(db.Date)
    condiciones = db.Column(db.Text)
    activo = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Promocion {self.nombre} - {self.descuento}%>"

    def is_valid_for(self, date):
        """Valida si la promoción aplica para una fecha dada."""
        if not self.activo:
            return False
        if self.fecha_inicio and date < self.fecha_inicio:
            return False
        if self.fecha_fin and date > self.fecha_fin:
            return False
        return True

    def apply_discount(self, amount):
        """Aplica descuento porcentual a un monto y devuelve monto descontado."""
        return amount * (self.descuento / 100.0)
