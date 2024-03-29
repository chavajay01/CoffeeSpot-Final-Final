from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.auth import auth
from routes.recursos import Recursos
from routes.todolist import todolist
from routes.inventario import Inventario
from routes.ventas import Ventas
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from utils.loginManagerService import login_manager
from utils.db import db

app = Flask(__name__)

app.config.from_object("config.BaseConfig")

SQLAlchemy(app)
Bcrypt(app)
login_manager.init_app(app)
Migrate(app, db)

app.register_blueprint(auth)
app.register_blueprint(Recursos)
app.register_blueprint(Inventario)
app.register_blueprint(Ventas)
app.register_blueprint(todolist)


