from datetime import datetime
from app.extensions import db

class PoliticaPago(db.Model):
    """
    Politica de pago asociada a un hotel.
    tipo: 'anticipado', 'al_checkin', 'parcial', etc.
    condiciones: texto explicativo o JSON con reglas.
    """
    __tablename__ = 'politicas_pago'

    id = db.Column(db.Integer, primary_key=True)
    hotel_id = db.Column(db.Integer, db.ForeignKey('hoteles.id'), nullable=False, unique=True)
    tipo = db.Column(db.String(50), nullable=False)
    condiciones = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<PoliticaPago {self.tipo} - hotel {self.hotel_id}>"

    def requires_prepayment(self):
        """Ejemplo de regla: devolvemos True si tipo implica pago anticipado completo."""
        return self.tipo.lower() in ['anticipado', 'prepaid']
