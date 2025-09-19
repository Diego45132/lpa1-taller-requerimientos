from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Habitacion, Cliente, Reserva
from datetime import datetime

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/habitaciones')
def habitaciones():
    habitaciones = Habitacion.query.all()
    return render_template('habitaciones.html', habitaciones=habitaciones)


@main_bp.route('/reservas', methods=['GET', 'POST'])
def reservas():
    if request.method == 'POST':
        cliente_id = request.form.get('cliente_id')
        habitacion_id = request.form.get('habitacion_id')
        fecha_inicio = request.form.get('fecha_inicio')
        fecha_fin = request.form.get('fecha_fin')
        if not (cliente_id and habitacion_id and fecha_inicio and fecha_fin):
            flash('Todos los campos son obligatorios.', 'danger')
        else:
            try:
                reserva = Reserva(
                    cliente_id=int(cliente_id),
                    habitacion_id=int(habitacion_id),
                    fecha_inicio=datetime.strptime(fecha_inicio, '%Y-%m-%d'),
                    fecha_fin=datetime.strptime(fecha_fin, '%Y-%m-%d'),
                    estado='pendiente'
                )
                from app.extensions import db
                db.session.add(reserva)
                db.session.commit()
                flash('Reserva registrada correctamente.', 'success')
                return redirect(url_for('main.reservas'))
            except Exception as e:
                flash(f'Error al registrar reserva: {e}', 'danger')
    reservas = Reserva.query.all()
    clientes = Cliente.query.all()
    habitaciones = Habitacion.query.all()
    return render_template('reservas.html', reservas=reservas, clientes=clientes, habitaciones=habitaciones)

@main_bp.route('/clientes', methods=['GET', 'POST'])
def clientes():
    from app.extensions import db
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        telefono = request.form.get('telefono')
        direccion = request.form.get('direccion')
        if not (nombre and email):
            flash('Nombre y email son obligatorios.', 'danger')
        else:
            try:
                cliente = Cliente(nombre=nombre, email=email, telefono=telefono, direccion=direccion)
                db.session.add(cliente)
                db.session.commit()
                flash('Cliente registrado correctamente.', 'success')
                return redirect(url_for('main.clientes'))
            except Exception as e:
                flash(f'Error al registrar cliente: {e}', 'danger')
    clientes = Cliente.query.all()
    return render_template('clientes.html', clientes=clientes)

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@main_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    return render_template('registro.html')
