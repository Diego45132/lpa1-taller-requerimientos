from flask import Blueprint, render_template
from app.models import Habitacion, Cliente, Reserva

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/habitaciones')
def habitaciones():
    habitaciones = Habitacion.query.all()
    return render_template('habitaciones.html', habitaciones=habitaciones)

@main_bp.route('/reservas')
def reservas():
    reservas = Reserva.query.all()
    return render_template('reservas.html', reservas=reservas)

@main_bp.route('/clientes')
def clientes():
    clientes = Cliente.query.all()
    return render_template('clientes.html', clientes=clientes)

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@main_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    return render_template('registro.html')
