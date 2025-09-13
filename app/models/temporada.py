from datetime import datetime
from app.extensions import db

class Temporada(db.Model):
    """
    Temporada (ej. alta/baja). Se puede usar para ajustar precios por factor.
    """
    __tablename__ = 'temporadas'

    id = db.Column(db.Integer, primary_key=True)
    hotel_id = db.Column(db.Integer, db.ForeignKey('hoteles.id'), nullable=True)
    nombre = db.Column(db.String(100), nullable=False)
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_fin = db.Column(db.Date, nullable=False)
    region = db.Column(db.String(255))
    factor_precio = db.Column(db.Float, default=1.0)  # multiplicador a aplicar sobre precio_base

    def __repr__(self):
        return f"<Temporada {self.nombre} ({self.fecha_inicio} - {self.fecha_fin})>"

    def includes(self, date):
        """Retorna True si la fecha está dentro de la temporada."""
        return self.fecha_inicio <= date <= self.fecha_fin
