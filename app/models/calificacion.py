from datetime import datetime
from app.extensions import db

class Calificacion(db.Model):
    """
    Comentarios y calificaciones dejadas por clientes tras su estancia.
    Solo clientes con reservas finalizadas deberían poder crear calificaciones.
    """
    __tablename__ = 'calificaciones'

    id = db.Column(db.Integer, primary_key=True)
    reserva_id = db.Column(db.Integer, db.ForeignKey('reservas.id'), nullable=False)
    habitacion_id = db.Column(db.Integer, db.ForeignKey('habitaciones.id'), nullable=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    puntaje = db.Column(db.Integer, nullable=False)  # 1..5
    comentario = db.Column(db.Text)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Calificacion {self.puntaje} reserva {self.reserva_id}>"

    @classmethod
    def create(cls, reserva, cliente, puntaje, comentario=None):
        """
        Crea una calificación asociada a una reserva; validar que la reserva esté finalizada
        (estado confirmada y fecha_fin pasada) corresponde al caller.
        """
        cal = cls(
            reserva_id=reserva.id,
            habitacion_id=reserva.habitacion_id,
            cliente_id=cliente.id,
            puntaje=puntaje,
            comentario=comentario
        )
        db.session.add(cal)
        db.session.commit()
        return cal
