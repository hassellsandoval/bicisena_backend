from datetime import datetime
from flask import Blueprint, jsonify, request
from models.models import Alquiler, Usuarios, Bicicletas
from app import db

# --------------------------------------------------------------------- #
# Rutas para las usuarios
# --------------------------------------------------------------------- #

usuarios_users = Blueprint("usuarios_users", __name__)

@usuarios_users.get("/users/usuarios")
def obtener_usuarios():
    usuarios = Usuarios.query.all()
    lista_usuarios = [
        {
            "id_usuarios": usuario.id_usuarios,
            "nombres": usuario.nombres,
            "direccion": usuario.direccion,
            "barrio": usuario.barrio,
            "ciudad": usuario.ciudad,
            "departamento": usuario.departamento,
            "email": usuario.email,
            "password": usuario.password,
            "estrato": usuario.estrato,
        }
        for usuario in usuarios
    ]
    return jsonify(lista_usuarios)


@usuarios_users.get("/users/usuarios/<int:id>")
def obtener_usuario_por_id(id):
    usuario = Usuarios.query.get_or_404(id, description="usuario no encontrada")
    if not usuario:
        return jsonify({"message": "usuario no encontrada"}), 404
    return jsonify(
        {
            "id_usuarios": usuario.id_usuarios,
            "nombres": usuario.nombres,
            "direccion": usuario.direccion,
            "barrio": usuario.barrio,
            "ciudad": usuario.ciudad,
            "departamento": usuario.departamento,
            "email": usuario.email,
            "password": usuario.password,
            "rol": usuario.rol,
            "estrato": usuario.estrato
        }
    )

@usuarios_users.patch('/users/usuarios/<int:id>')
def actualizar_usuario(id):
    usuario = Usuarios.query.get(id)
    if not usuario:
        return jsonify({'message': 'usuario no encontrada'}), 404
    data = request.json
    usuario.nombres = data['nombres']
    usuario.direccion = data['direccion']
    usuario.barrio = data['barrio']
    usuario.ciudad = data['ciudad']
    usuario.departamento = data['departamento']
    usuario.email = data['email']
    usuario.password = data['password']
    usuario.rol = data['rol']
    usuario.estrato = data['estrato']
    db.session.commit()
    return jsonify({'message': 'usuario actualizada satisfactoriamente'}), 200

# --------------------------------------------------------------------- #
# Rutas para las bicicletas
# --------------------------------------------------------------------- #

bicicletas_users = Blueprint("bicicletas_users", __name__)

@bicicletas_users.get("/users/bicicletas")
def obtener_bicicletas():
    bicicletas = Bicicletas.query.all()
    lista_bicicletas = [
        {
            "id_bicicletas": bicicleta.id_bicicletas,
            "serial": bicicleta.serial,
            "color": bicicleta.color,
            "marca": bicicleta.marca,
            "estado": bicicleta.estado,
            "disponibilidad": bicicleta.disponibilidad,
            "url_imagen": bicicleta.url_imagen,
            "coordenada_x": bicicleta.coordenada_x,
            "coordenada_y": bicicleta.coordenada_y,
            "id_regionales": bicicleta.id_regionales,
        }
        for bicicleta in bicicletas
    ]
    return jsonify(lista_bicicletas)


@bicicletas_users.get("/users/bicicletas/<int:id>")
def obtener_bicicleta_por_id(id):
    bicicleta = Bicicletas.query.get_or_404(id, description="bicicleta no encontrada")
    if not bicicleta:
        return jsonify({"message": "bicicleta no encontrada"}), 404
    return jsonify(
        {
            "id_bicicletas": bicicleta.id_bicicletas,
            "serial": bicicleta.serial,
            "color": bicicleta.color,
            "marca": bicicleta.marca,
            "estado": bicicleta.estado,
            "disponibilidad": bicicleta.disponibilidad,
            "url_imagen": bicicleta.url_imagen,
            "coordenada_x": bicicleta.coordenada_x,
            "coordenada_y": bicicleta.coordenada_y,
            "id_regionales": bicicleta.id_regionales,
        }
    )

# --------------------------------------------------------------------- #
# Rutas para el alquiler
# --------------------------------------------------------------------- #

alquiler_routes = Blueprint("alquiler_routes", __name__)

@alquiler_routes.get("/alquiler")
def obtener_alquileres():
    alquileres = Alquiler.query.all()
    lista_alquileres = [alquiler.to_dict() for alquiler in alquileres]
    return jsonify(lista_alquileres)

@alquiler_routes.get("/alquiler/<int:id>")
def obtener_alquiler_por_id(id):
    alquiler = Alquiler.query.get_or_404(id, description="Alquiler no encontrado")
    return jsonify(alquiler.to_dict())

@alquiler_routes.post("/alquiler")
def crear_alquiler():
    data = request.json
    nuevo_alquiler = Alquiler(
        tarifa_base=data['tarifa_base'],
        recorrido=data['recorrido'],
        hora_incio=datetime.strptime(data['hora_incio'], '%H:%M:%S').time(),
        hora_fin=datetime.strptime(data['hora_fin'], '%H:%M:%S').time(),
        fecha_alquiler=datetime.strptime(data['fecha_alquiler'], '%Y-%m-%d').date(),
        tarifa_total=data['tarifa_total'],
        id_usuarios=data['id_usuarios'],
        id_bicicletas=data['id_bicicletas']
    )
    db.session.add(nuevo_alquiler)
    db.session.commit()
    return jsonify({"message": "Alquiler creado satisfactoriamente", "id": nuevo_alquiler.id_alquier}), 201

@alquiler_routes.patch('/alquiler/<int:id>')
def actualizar_alquiler(id):
    alquiler = Alquiler.query.get_or_404(id, description="Alquiler no encontrado")
    data = request.json
    for key, value in data.items():
        if key in ['hora_incio', 'hora_fin']:
            setattr(alquiler, key, datetime.strptime(value, '%H:%M:%S').time())
        elif key == 'fecha_alquiler':
            setattr(alquiler, key, datetime.strptime(value, '%Y-%m-%d').date())
        else:
            setattr(alquiler, key, value)
    db.session.commit()
    return jsonify({"message": "Alquiler actualizado satisfactoriamente"}), 200

@alquiler_routes.delete('/alquiler/<int:id>')
def eliminar_alquiler(id):
    alquiler = Alquiler.query.get_or_404(id, description="Alquiler no encontrado")
    db.session.delete(alquiler)
    db.session.commit()
    return jsonify({"message": "Alquiler eliminado satisfactoriamente"}), 200

@alquiler_routes.get("/alquiler/usuario/<int:id_usuario>")
def obtener_alquileres_por_usuario(id_usuario):
    """Obtiene todos los alquileres de un usuario específico."""
    alquileres = Alquiler.query.filter_by(id_usuarios=id_usuario).all()
    return jsonify([alquiler.to_dict() for alquiler in alquileres])

@alquiler_routes.get("/alquiler/bicicleta/<int:id_bicicleta>")
def obtener_alquileres_por_bicicleta(id_bicicleta):
    """Obtiene el historial de alquileres de una bicicleta específica."""
    alquileres = Alquiler.query.filter_by(id_bicicletas=id_bicicleta).all()
    return jsonify([alquiler.to_dict() for alquiler in alquileres])

@alquiler_routes.get("/alquiler/periodo")
def obtener_alquileres_por_periodo():
    """Obtiene alquileres en un período de tiempo específico."""
    fecha_inicio = request.args.get('fecha_inicio')
    fecha_fin = request.args.get('fecha_fin')
    
    if not fecha_inicio or not fecha_fin:
        return jsonify({"error": "Se requieren fecha_inicio y fecha_fin"}), 400
    
    try:
        fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d').date()
        fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({"error": "Formato de fecha inválido. Use YYYY-MM-DD"}), 400
    
    alquileres = Alquiler.query.filter(
        Alquiler.fecha_alquiler.between(fecha_inicio, fecha_fin)
    ).all()
    
    return jsonify([alquiler.to_dict() for alquiler in alquileres])