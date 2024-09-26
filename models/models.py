from datetime import date
from time import time
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, Enum, Numeric, String, Boolean, DateTime, Time, func
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app import db
from enums.estrato import Estrato
from enums.rol import Rol
from typing import List

# -------------------------------------------------------------------------------------------------------- #
# Modelos para las usuarios
# -------------------------------------------------------------------------------------------------------- #

class Usuarios(db.Model):  # Usa db.Model como base para las clases
    __tablename__ = 'usuarios'

    id_usuarios: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombres: Mapped[str] = mapped_column(String(255), nullable=False)
    direccion: Mapped[str] = mapped_column(String(255), nullable=False)
    barrio: Mapped[str] = mapped_column(String(255), nullable=False)
    ciudad: Mapped[str] = mapped_column(String(255), nullable=False)
    departamento: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    rol: Mapped[Rol] = mapped_column(Enum(Rol), nullable=False, default=Rol.USUARIO)
    estrato: Mapped[str] = mapped_column(String(255), nullable=False)

    usuarios_ciclopaseo: Mapped[list["UsuariosCiclopaseo"]] = relationship(back_populates="usuarios")
    alquiler: Mapped[list["Alquiler"]] = relationship(back_populates="usuarios")  # type: ignore # type: ignore


    def to_dict(self):
        return {
            'id_usuarios': self.id_usuarios,
            'nombres': self.nombres,
            'direccion': self.direccion,
            'barrio': self.barrio,
            'ciudad': self.ciudad,
            'departamento': self.departamento,
            'email': self.email,
            'rol': self.rol.value,
            'estrato': self.estrato
        }
    
    def __repr__(self):
        return f'<Nombres {self.nombres!r}, <Direccion {self.direccion!r}, <Barrio {self.barrio!r}, <Ciudad {self.ciudad!r}, <Departamento {self.departamento!r}, <Email {self.email!r}, <Password {self.password!r}, <Rol {self.rol!r}>, <Estrato {self.estrato!r}, <Sede {self.sede!r}>'

# --------------------------------------------------------------------- #
# Modelos para el alquiler
# --------------------------------------------------------------------- #

class Alquiler(db.Model):
    __tablename__ = "alquiler"

    id_alquier: Mapped[int] = mapped_column(primary_key=True)
    tarifa_base: Mapped[float] = mapped_column(Float, nullable=False)
    recorrido: Mapped[float] = mapped_column(Float, nullable=False)
    hora_incio: Mapped[time] = mapped_column(Time, nullable=False)
    hora_fin: Mapped[time] = mapped_column(Time, nullable=False)
    fecha_alquiler: Mapped[date] = mapped_column(Date, nullable=False)
    tarifa_total: Mapped[float] = mapped_column(Float, nullable=False)
    id_usuarios: Mapped[int] = mapped_column(Integer, ForeignKey("usuarios.id_usuarios"))
    id_bicicletas: Mapped[int] = mapped_column(Integer, ForeignKey("bicicletas.id_bicicletas"))

    usuarios: Mapped["Usuarios"] = relationship(back_populates="alquiler")
    bicicletas: Mapped["Bicicletas"] = relationship(back_populates="alquiler")

    def to_dict(self):
        return {
            "tarifa_base": self.tarifa_base,
            "recorrido": self.recorrido,
            "hora_incio": self.hora_incio,
            "hora_fin": self.hora_fin,
            "fecha_alquiler": self.fecha_alquiler,
            "tarifa_total": self.tarifa_total,
            "id_usuario": self.id_usuario,
            "id_bicicletas": self.id_bicicletas,
        }

    def __repr__(self):        
        return f'<Tarifa_base {self.tarifa_base!r}>'

# --------------------------------------------------------------------- #
# Modelos para bicicletas
# --------------------------------------------------------------------- #

class Bicicletas(db.Model):
    __tablename__ = "bicicletas"

    id_bicicletas: Mapped[int] = mapped_column(primary_key=True)
    serial: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    color: Mapped[str] = mapped_column(String(1000))
    marca: Mapped[str] = mapped_column(String(255), nullable=False)
    estado: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    disponibilidad: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    url_imagen: Mapped[str] = mapped_column(String(255))
    coordenada_x: Mapped[float] = mapped_column(Float, nullable=False)
    coordenada_y: Mapped[float] = mapped_column(Float, nullable=False)
    id_regionales: Mapped[int] = mapped_column(Integer, ForeignKey("regionales.id_regionales"))
    
    regionales: Mapped["Regionales"] = relationship(back_populates="bicicletas")
    alquiler: Mapped[list["Alquiler"]] = relationship(back_populates="bicicletas")


    def to_dict(self):
        return {

                "id_bicicletas": self.id_bicicletas,
                "serial": self.serial,
                "color": self.color,
                "marca": self.marca,
                "estado": self.estado,
                "disponibilidad": self.disponibilidad,
                "url_imagen": self.url_imagen,
                "coordenada_x": self.coordenada_x,
                "coordenada_y": self.coordenada_y,
                "id_regionales": self.id_regionales,
        }

    def __repr__(self):
        return f'<Nombre {self.nombre!r}, <Marca {self.marca!r}, <Color {self.color!r}, <IsActivo {self.is_activo!r}, <URLImagen {self.url_imagen!r}, <Cantidad {self.cantidad!r}, <Stock {self.stock!r}>'

# -------------------------------------------------------------------------------------------------------- #
# Modelos para las regionales
# -------------------------------------------------------------------------------------------------------- #

class Regionales(db.Model):  # Usa db.Model como base para las clases
    __tablename__ = 'regionales'

    id_regionales: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(255), nullable=False)
    bicicletas: Mapped[List["Bicicletas"]] = relationship("Bicicletas", back_populates="regionales")

    def to_dict(self):
        return {
            "nombre": self.nombre
        }
    
    def __repr__(self):
        return f'<Nombre {self.nombre!r}>'


# -------------------------------------------------------------------------------------------------------- #
# Modelos para ternaria usuarios_ciclopaseo
# -------------------------------------------------------------------------------------------------------- #

class UsuariosCiclopaseo(db.Model):  # Usa db.Model como base para las clases
    __tablename__ = 'usuarios_ciclopaseo'

    id_usuciclo: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_usuario: Mapped[int] = mapped_column(Integer, ForeignKey("usuarios.id_usuarios"))
    id_ciclopaseo: Mapped[int] = mapped_column(Integer, ForeignKey("ciclopaseo.id_ciclopaseo"))

    usuarios: Mapped["Usuarios"] = relationship(back_populates="usuarios_ciclopaseo")
    ciclopaseo: Mapped["ciclopaseo"] = relationship(back_populates="usuarios_ciclopaseo")

    def to_dict(self):
        return {
            "id_usuario": self.id_usuario,
            "id_ciclopaseo": self.id_ciclopaseo,
        }
    
    def __repr__(self):
        return f'<id_usuario {self.id_usuario!r}, <id_ciclopaseo {self.id_ciclopaseo!r}>'
    
# -------------------------------------------------------------------------------------------------------- #
# Modelos para los ciclopaseos
# -------------------------------------------------------------------------------------------------------- #
   
class ciclopaseo(db.Model):  # Usa db.Model como base para las clases
    __tablename__ = 'ciclopaseo'

    id_ciclopaseo: Mapped[int] = mapped_column(Integer, primary_key=True)
    titulo: Mapped[str] = mapped_column(String(255), nullable=False)
    descripciòn: Mapped[str] = mapped_column(String(255), nullable=False)
    url_imagen: Mapped[str] = mapped_column(String(255))
    direccion: Mapped[str] = mapped_column(String(255), nullable=False)
    fecha: Mapped[date] = mapped_column(Date, nullable=False)

    usuarios_ciclopaseo: Mapped[list["UsuariosCiclopaseo"]] = relationship(back_populates="ciclopaseo")


    def to_dict(self):
        return {
            "titulo": self.titulo,
            "descripciòn": self.descripciòn,
            "url_imagen": self.url_imagen,
            "direccion": self.direccion,
            "fecha": self.fecha
        }
    
    def __repr__(self):
        return f'<Nombre {self.titulo!r}, <Descripción {self.descripción!r}, <URLImagen {self.url_imagen!r}>, <Direccion {self.direccion!r}, <Fecha {self.fecha!r}>'