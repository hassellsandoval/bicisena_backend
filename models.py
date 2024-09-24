from datetime import date, datetime
from sqlalchemy import Date, Float, ForeignKey, Integer, Enum, Numeric, String, Boolean, DateTime, func
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app import db
from enums.estrato import Estrato
from enums.rol import Rol
from enums.metodo_pago import Metodo_Pago
from typing import List


# -------------------------------------------------------------------------------------------------------- #
# Modelos para las usuarios
# -------------------------------------------------------------------------------------------------------- #

class Usuarios(db.Model):  # Usa db.Model como base para las clases
    __tablename__ = 'usuarios'

    id_usuarios: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombres: Mapped[str] = mapped_column(String(255), nullable=False)
    apellidos: Mapped[str] = mapped_column(String(255), nullable=False)
    direccion: Mapped[str] = mapped_column(String(255), nullable=False)
    barrio: Mapped[str] = mapped_column(String(255), nullable=False)
    ciudad: Mapped[str] = mapped_column(String(255), nullable=False)
    departamento: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    rol: Mapped[Rol] = mapped_column(Enum(Rol), nullable=False)
    estrato: Mapped[Estrato] = mapped_column(Enum(Estrato), nullable=False)

    child: Mapped["Bicicletas"] = relationship(back_populates="id_usuarios", cascade="all, delete-orphan")  # type: ignore
    children: Mapped[List["Alquiler"]] = relationship(back_populates="id_usuario", cascade="all, delete-orphan")  # type: ignore

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "apellidos": self.apellidos,
            "direccion": self.direccion,
            "barrio": self.barrio,
            "ciudad": self.ciudad,
            "departamento": self.departamento,
            "email": self.email,
            "password": self.password,
            "rol": self.rol,
            "estrato": self.estrato,
            "sede": self.sede,
        }
    
    def __repr__(self):
        return f'<Nombre {self.nombre!r}, <Apellidos {self.apellidos!r}, <Direccion {self.direccion!r}, <Barrio {self.barrio!r}, <Ciudad {self.ciudad!r}, <Departamento {self.departamento!r}, <Email {self.email!r}, <Password {self.password!r}, <Rol {self.rol!r}>, <Estrato {self.estrato!r}, <Sede {self.sede!r}>'


# --------------------------------------------------------------------- #
# Modelos para bicicletas
# --------------------------------------------------------------------- #

class Bicicletas(db.Model):
    __tablename__ = "bicicletas"

    id: Mapped[int] = mapped_column(primary_key=True)
    serial: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    marca: Mapped[str] = mapped_column(String(255), nullable=False)
    color: Mapped[str] = mapped_column(String(1000))
    is_activo: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    url_imagen: Mapped[str] = mapped_column(String(255))
    cantidad: Mapped[int] = mapped_column(Integer)
    stock: Mapped[int] = mapped_column(Integer, nullable=False)
    id_usuario: Mapped[int] = mapped_column(Integer, ForeignKey("usuarios.id_usuarios"))

    parent: Mapped["Usuarios"] = relationship(back_populates="bicicletas", cascade="all, delete-orphan")  # type: ignore


    def to_dict(self):
        return {
            "id": self.id,
            "code": self.code,
            "marca": self.marca,
            "color": self.color,
            "is_activo": self.is_activo,
            "url_imagen": self.url_imagen,
            "cantidad": self.cantidad,
            "stock": self.stock,
        }

    def __repr__(self):        
        return f'<Nombre {self.nombre!r}, <Marca {self.marca!r}, <Color {self.color!r}, <IsActivo {self.is_activo!r}, <URLImagen {self.url_imagen!r}, <Cantidad {self.cantidad!r}, <Stock {self.stock!r}>'
    
# --------------------------------------------------------------------- #
# Modelos para el alquiler
# --------------------------------------------------------------------- #

class Alquiler(db.Model):
    __tablename__ = "alquiler"

    id_alquier: Mapped[int] = mapped_column(primary_key=True)
    tarifa_base: Mapped[float] = mapped_column(Float, nullable=False)
    recorrido: Mapped[float] = mapped_column(Float, nullable=False)
    hora_incio: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    hora_fin: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    fecha_alquiler: Mapped[date] = mapped_column(Date, nullable=False)
    tarifa_total: Mapped[float] = mapped_column(Float, nullable=False)
    metodo_pago: Mapped[Metodo_Pago] = mapped_column(Enum(Metodo_Pago), nullable=False)
    id_usuario: Mapped[int] = mapped_column(Integer, ForeignKey("usuarios.id_usuarios"))

    parent: Mapped["Usuarios"] = relationship(back_populates="alquiler", cascade="all, delete-orphan")  # type: ignore


    def to_dict(self):
        return {
            "tarifa_base": self.tarifa_base
        }

    def __repr__(self):        
        return f'<Tarifa_base {self.tarifa_base!r}>'
    
# -------------------------------------------------------------------------------------------------------- #
# Modelos para factura
# -------------------------------------------------------------------------------------------------------- #

class Sedes(db.Model):  # Usa db.Model como base para las clases
    __tablename__ = 'sedes'

    id_factura: Mapped[int] = mapped_column(Integer, primary_key=True)
    num_factura: Mapped[int] = mapped_column(Integer(255), nullable=False)
    nombre: Mapped[str] = mapped_column(String(255), nullable=False)
    fecha: Mapped[date] = mapped_column(Date, nullable=False)
    id_bicicleta: Mapped[int] = mapped_column(Integer, ForeignKey("bicicletas.id"))


    def to_dict(self):
        return {
            "nombre": self.nombre,
            "direccion": self.direccion,
            "barrio": self.barrio
        }
    
    def __repr__(self):
        return f'<Nombre {self.nombre!r}, <Direccion {self.direccion!r}, <Barrio {self.barrio!r}>'
    
# -------------------------------------------------------------------------------------------------------- #
# Modelos para las regionales
# -------------------------------------------------------------------------------------------------------- #

class Regionales(db.Model):  # Usa db.Model como base para las clases
    __tablename__ = 'regionales'

    id_regional: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(255), nullable=False)

    def to_dict(self):
        return {
            "nombre": self.nombre
        }
    
    def __repr__(self):
        return f'<Nombre {self.nombre!r}>'


# -------------------------------------------------------------------------------------------------------- #
# Modelos para las ciudades
# -------------------------------------------------------------------------------------------------------- #

class Ciudades(db.Model):  # Usa db.Model como base para las clases
    __tablename__ = 'ciudades'

    id_ciudad: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(255), nullable=False)

    def to_dict(self):
        return {
            "nombre": self.nombre
        }
    
    def __repr__(self):
        return f'<Nombre {self.nombre!r}>'
    
# -------------------------------------------------------------------------------------------------------- #
# Modelos para las sedes
# -------------------------------------------------------------------------------------------------------- #
   
class Sedes(db.Model):  # Usa db.Model como base para las clases
    __tablename__ = 'sedes'

    id_sede: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(255), nullable=False)
    direccion: Mapped[str] = mapped_column(String(255), nullable=False)
    barrio: Mapped[str] = mapped_column(String(255), nullable=False)

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "direccion": self.direccion,
            "barrio": self.barrio
        }
    
    def __repr__(self):
        return f'<Nombre {self.nombre!r}, <Direccion {self.direccion!r}, <Barrio {self.barrio!r}>'