from flask import Blueprint, jsonify, request
from models.models import Usuarios, Bicicletas
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