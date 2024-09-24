from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# -------------------------------------------------------------------- #
# COnfiguración CORS
# -------------------------------------------------------------------- #
CORS(app)

# -------------------------------------------------------------------- #
# Configuración SQLAlchemy
# -------------------------------------------------------------------- #
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:1234@localhost:3307/bicisena?charset=utf8mb4"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

# -------------------------------------------------------------------- #
# Inicialización de SQLAlchemy con la aplicación
# -------------------------------------------------------------------- #
db = SQLAlchemy(app)

# -------------------------------------------------------------------- #
# Importaciónd de los blueprints de cada una de las rutas
# -------------------------------------------------------------------- #
# --> from routes import usuarios

# -------------------------------------------------------------------- #
# Creación de las tablas en la base de datos a través de los modelos con SQLAlchemy
# -------------------------------------------------------------------- #
with app.app_context():
    from models import *

    db.create_all()

# -------------------------------------------------------------------- #
# Registro de Blueprints rutas publicas
# -------------------------------------------------------------------- #
# --> app.register_blueprint(usuarios)

@app.route("/")
def hello_world():
    return "<p>Hola, Soy una pequeña api</p>"
