from datetime import datetime
from app.extensions import db

class PoliticaCancelacion(db.Model):
    """
    Política de cancelación.
    tipo: 'reembolsable', 'parcial', 'no_reembolsable'
    penalidad: porcentaje aplicado en caso de penalidad
    condiciones: texto explicativo
    """
    __tablename__ = 'politicas_cancelacion'

    id = db.Column(db.Integer, primary_key=True)
    hotel_id = db.Column(db.Integer, db.ForeignKey('hoteles.id'), nullable=False, unique=True)
    tipo = db.Column(db.String(50), nullable=False)
    penalidad = db.Column(db.Float, default=0.0)  # porcentaje (ej. 20.0)
    condiciones = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<PoliticaCancelacion {self.tipo} - hotel {self.hotel_id}>"

    def calculate_refund(self, monto, dias_antes):
        """
        Calcula monto de reembolso teniendo en cuenta penalidad.
        La lógica puede variar según dias_antes; aquí un modelo simple:
        """
        if self.tipo == 'no_reembolsable':
            return 0.0
        if self.tipo == 'parcial':
            # penalidad porcentual
            return monto * (1 - (self.penalidad / 100.0))
        # reembolsable
        return monto
