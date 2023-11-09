from flask import Blueprint,request,jsonify,render_template,redirect
from sqlalchemy import exc
from models import User
from app import db,bcrypt


appuser = Blueprint('appuser',__name__,template_folder='templates')

@appuser.route("/auth/registro",methods = ["POST"])
def registro():
    user  = request.get_json()
    userExists = User.query.filter_by(email=user["email"]).first()
    if not userExists:
        usuario = User(email=user['email'],password=user['password'])
        try:
            db.session.add(usuario)
            db.session.commit()
            mensaje="Usuario Creado"
        except exc.SQLAlchemyError as e:
            mensaje= "Error: " + e
    return jsonify({"Mensaje" : mensaje})

@appuser.route("/auth/login",methods=["POST"])
def login():
    user = request.get_json()
    usuario = User(email=user['email'],password=user['password'])
    searchUser = User.query.filter_by(email = usuario.email).first
    if searchUser:
        validation = bcrypt.check_password_hash(searchUser.password,user)
        if validation:
            auth_token = usuario.encode_auth_token(user_id=searchUser)
            response = {
                'status':'success',
                'message':'Login exitoso',
                'auth_token':auth_token
            }
            return jsonify(response)
    return jsonify({"message":'Datos incorrectos'})