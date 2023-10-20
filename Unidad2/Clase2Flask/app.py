from flask import Flask
from database import db
from config import BasicConf
from flask_migrate import Migrate
import logging
from rutas.persona.personas import appPersona
from rutas.producto.producto import approducto
from rutas.imagen.imagen import appimagen
app = Flask(__name__)
app.register_blueprint(appPersona)
app.register_blueprint(approducto)
app.register_blueprint(appimagen)
app.config.from_object(BasicConf)
db.init_app(app)
migrate =Migrate()
migrate.init_app(app,db)
logging.basicConfig(level=logging.DEBUG,filename="logs.log")