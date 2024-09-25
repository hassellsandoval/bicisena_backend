from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# -------------------------------------------------------------------- #
# Configuración CORS
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
from routes.public.public_routes import usuarios_public
from routes.users.user_routes import usuarios_users
from routes.admin.admin_routes import usuarios_admin
# -------------------------------------------------------------------- #
# Creación de las tablas en la base de datos a través de los modelos con SQLAlchemy
# -------------------------------------------------------------------- #
with app.app_context():
    from models.models import *

    db.create_all()

# -------------------------------------------------------------------- #
# Registro de Blueprints rutas publicas
# -------------------------------------------------------------------- #
# --> app.register_blueprint(usuarios)

@app.route("/")
def hello_world():
    return "<p>Hola, Soy una pequeña api de bicicletas</p>"
