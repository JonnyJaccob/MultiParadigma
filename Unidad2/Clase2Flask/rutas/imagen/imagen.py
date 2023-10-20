from flask import Blueprint,request,render_template

from models import Images
from app import db 
import base64 

appimagen = Blueprint("appimagen",__name__,template_folder = "vistas")

def renderImage(data):
    imagenRenderizada = base64.b64encode(data)
    return imagenRenderizada

@appimagen.route('/leerImagen/<int:id>')
def leerImagen(id):
    imagen = Images.query.filter_by(id=id).first().renderData
    return render_template('mostrasImagen.html',imagen=imagen)

@appimagen.route('/leerImagen')
def indexImagen():
    if request.method=="POST":
        file = request.files['img']
        data = file.read()
        render = renderImage(data)
        nuevaImagen = Images()
        nuevaImagen.type = "Perfil"
        nuevaImagen.renderData = render 
        nuevaImagen.data = data 
        db.session.add(nuevaImagen)
        db.session.commit()
    return render_template('imagenes.html')  