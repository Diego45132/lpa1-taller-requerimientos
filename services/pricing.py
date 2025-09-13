from datetime import date
from app.extensions import db
from app.models.temporada import Temporada
from app.models.promocion import Promocion

def find_applicable_temporada(hotel, start_date):
    """
    Busca la temporada que aplica para una fecha en un hotel.
    """
    return hotel.temporadas.filter(
        Temporada.fecha_inicio <= start_date,
        Temporada.fecha_fin >= start_date
    ).first()

def find_applicable_promocion(hotel, date):
    """
    Retorna la primera promoción válida para la fecha dada.
    """
    for promo in hotel.promociones:
        if promo.is_valid_for(date):
            return promo
    return None
