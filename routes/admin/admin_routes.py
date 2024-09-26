from flask import Blueprint, jsonify, request
from models.models import Usuarios, Bicicletas
from app import db

# --------------------------------------------------------------------- #
# Rutas para las usuarios
# --------------------------------------------------------------------- #

usuarios_admin = Blueprint("usuarios_admin", __name__)

@usuarios_admin.get("admin/usuarios")
def obtener_usuarios():
    usuarios = usuarios.query.all()
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
            "rol": usuario.rol,
            "estrato": usuario.estrato,
        }
        for usuario in usuarios
    ]
    return jsonify(lista_usuarios)


@usuarios_admin.get("admin/usuarios/<int:id>")
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

@usuarios_admin.post("admin/usuarios")
def guardar_usuarios():
    data = request.json
    nuevo_usuario = Usuarios(   nombres=data['nombres'],
    
                                direccion=data['direccion'],
                                barrio=data['barrio'],
                                ciudad=data['ciudad'],
                                departamento=data['departamento'],
                                email=data['email'],
                                password=data['password'],
                                rol=data['rol'],
                                estrato=data['estrato'],)
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({'message': 'Nueva usuario creada correctamente'}), 201

@usuarios_admin.patch('admin/usuarios/<int:id>')
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

@usuarios_admin.delete('admin/usuarios/<int:id>')
def eliminar_usuario(id):
    usuario = Usuarios.query.get(id)
    if not usuario:
        return jsonify({'message': 'usuario no encontrada'}), 404
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'message': 'La usuario ha sido eliminada satisactoriamnete'}), 200

# --------------------------------------------------------------------- #
# Rutas para las bicicletas
# --------------------------------------------------------------------- #

bicicletas_admin = Blueprint("bicicletas_admin", __name__)

@bicicletas_admin.get("admin/bicicletas")
def obtener_bicicletas():
    bicicletas = bicicletas.query.all()
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


@bicicletas_admin.get("admin/bicicletas/<int:id>")
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

@bicicletas_admin.post("admin/bicicletas")
def guardar_bicicletas():
    data = request.json
    nuevo_bicicleta = Bicicletas(   serial=data['serial'],
                                    color=data['color'],
                                    marca=data['marca'],
                                    estado=data['estado'],
                                    disponibilidad=data['disponibilidad'],
                                    url_imagen=data['url_imagen'],
                                    coordenada_x=data['coordenada_x'],
                                    coordenada_y=data['coordenada_y'],
                                    id_regionales=data['id_regionales'],
                                )
    db.session.add(nuevo_bicicleta)
    db.session.commit()
    return jsonify({'message': 'Nueva bicicleta creada correctamente'}), 201

@bicicletas_admin.patch('admin/bicicletas/<int:id>')
def actualizar_bicicleta(id):
    bicicleta = Bicicletas.query.get(id)
    if not bicicleta:
        return jsonify({'message': 'bicicleta no encontrada'}), 404
    data = request.json
    bicicleta.serial = data['serial']
    bicicleta.color = data['color']
    bicicleta.marca = data['marca']
    bicicleta.estado = data['estado']
    bicicleta.disponibilidad = data['disponibilidad']
    bicicleta.url_imagen = data['url_imagen']
    bicicleta.coordenada_x = data['coordenada_x']
    bicicleta.coordenada_y = data['coordenada_y']
    db.session.commit()
    return jsonify({'message': 'bicicleta actualizada satisfactoriamente'}), 200

@bicicletas_admin.delete('admin/bicicletas/<int:id>')
def eliminarcategroias(id):
    bicicleta = Bicicletas.query.get(id)
    if not bicicleta:
        return jsonify({'message': 'bicicleta no encontrada'}), 404
    db.session.delete(bicicleta)
    db.session.commit()
    return jsonify({'message': 'La bicicleta ha sido eliminada satisactoriamnete'}), 200