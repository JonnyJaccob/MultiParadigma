from app import db
#formulario
class Persona(db.Model):
    #diferencia de django si se declara id
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    email = db.Column(db.String(250))
#puro json
class Producto(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    descripcion = db.Column(db.String(255))
    precio = db.Column(db.String(255))
    nombre = db.Column(db.String(255))
# formulario
class Images(db.Model):
    __tablename__ ="imagenes"
    id = db.Column(db.Integer,primary_key=True)
    type = db.Column(db.String(255),nullable=False)
    data = db.Column(db.LargeBinary,nullable=False)
    renderData = db.Column(db.Text,nullable=False)