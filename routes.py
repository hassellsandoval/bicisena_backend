from flask import Blueprint, jsonify, request
from models import usuarios, usuarios
from app import db

# --------------------------------------------------------------------- #
# Rutas para las usuarios
# --------------------------------------------------------------------- #

usuarios = Blueprint("usuarios", __name__)

@usuarios.get("/usuarios")
def obtener_usuarios():
    usuarios = usuarios.query.all()
    lista_usuarios = [
        {
            "id_usuarios": usuario.id_usuarios,
            "nombres": usuario.nombres,
            "apellidos": usuario.apellidos,
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


@usuarios.get("/usuarios/<int:id>")
def obtener_usuario_por_id(id):
    usuario = usuarios.query.get_or_404(id, description="usuario no encontrada")
    if not usuario:
        return jsonify({"message": "usuario no encontrada"}), 404
    return jsonify(
        {
            "id_usuarios": usuario.id_usuarios,
            "nombres": usuario.nombres,
            "apellidos": usuario.apellidos,
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

@usuarios.post("/usuarios")
def guardar_categroias():
    data = request.json
    nuevo_usuario = usuarios( nombre=data['nombre'], 
                                url_imagen=data['url_imagen'], )
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({'message': 'Nueva usuario creada correctamente'}), 201

@usuarios.patch('/usuarios/<int:id>')
def actualizarcategroias(id):
    usuario = usuarios.query.get(id)
    if not usuario:
        return jsonify({'message': 'usuario no encontrada'}), 404
    data = request.json
    usuario.nombres = data['nombres']
    usuario.apellidos = data['apellidos']
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

@usuarios.delete('/usuarios/<int:id>')
def eliminarcategroias(id):
    usuario = usuarios.query.get(id)
    if not usuario:
        return jsonify({'message': 'usuario no encontrada'}), 404
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'message': 'La usuario ha sido eliminada satisactoriamnete'}), 200