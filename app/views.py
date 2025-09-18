from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/habitaciones')
def habitaciones():
    return render_template('habitaciones.html')

@main_bp.route('/reservas')
def reservas():
    return render_template('reservas.html')

@main_bp.route('/clientes')
def clientes():
    return render_template('clientes.html')

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@main_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    return render_template('registro.html')
