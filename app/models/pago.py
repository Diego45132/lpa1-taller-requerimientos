# app/models/pago.py
from datetime import datetime
from datetime import datetime
from app.extensions import db

class Pago(db.Model):
    """
    Representa un pago asociado a una reserva.
    El método process_payment es un stub que se integraría con una pasarela real.
    """
    __tablename__ = 'pagos'

    id = db.Column(db.Integer, primary_key=True)
    reserva_id = db.Column(db.Integer, db.ForeignKey('reservas.id'), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    monto = db.Column(db.Float, nullable=False)
    metodo = db.Column(db.String(100))
    estado = db.Column(db.String(50), default='pendiente')  # pendiente, exitoso, fallido, reembolsado
    info_adicional = db.Column(db.Text)  # JSON con info de integración externa

    def __repr__(self):
        return f"<Pago {self.id} reserva {self.reserva_id} estado {self.estado}>"

    def process_payment(self, payment_info):
        """
        Procesa el pago: **stub**. Aquí se integraría con Stripe/PayPal.
        payment_info: dict con datos de la tarjeta o token.
        """
        # --- Simulación simple para desarrollo ---
        # Validar mínimo
        if self.monto <= 0:
            self.estado = 'fallido'
            db.session.commit()
            return False

        # Simular respuesta exitosa
        self.estado = 'exitoso'
        self.info_adicional = str(payment_info)
        db.session.commit()

        # Marcar reserva como confirmada (business rule)
        self.reserva.confirm()
        return True

    def refund(self, amount):
        """
        Simula un reembolso parcial/total. Actualiza estado a 'reembolsado' si completo.
        """
        # In a real integration, call the gateway refund API.
        # For now, mark as reembolsado si amount == monto
        if amount >= self.monto:
            self.estado = 'reembolsado'
        else:
            # registrar reembolso parcial en info_adicional (simplificado)
            self.info_adicional = (self.info_adicional or "") + f" | reembolso_partial:{amount}"
        db.session.commit()
        return True
