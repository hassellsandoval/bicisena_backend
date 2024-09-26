from flask import Blueprint, jsonify, request
from models.models import Usuarios
from app import db

# --------------------------------------------------------------------- #
# Rutas para las usuarios
# --------------------------------------------------------------------- #

usuarios_public = Blueprint("usuarios_public", __name__)

@usuarios_public.post("/public/registro/usuarios")
def registrar_usuarios():
    data = request.json
    nuevo_usuario = Usuarios(   nombres=data['nombres'],
                                direccion=data['direccion'],
                                barrio=data['barrio'],
                                ciudad=data['ciudad'],
                                departamento=data['departamento'],
                                email=data['email'],
                                password=data['password'],
                                #rol=data['rol'],
                                estrato=data['estrato'],)
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({'message': 'Nueva usuario creada correctamente'}), 201