from flask import Blueprint,jsonify,request
from models import Producto
from app import db

approducto = Blueprint("approducto",__name__)

@approducto.route('/producto/agregar',methods=["POST"])
def agregarProducto():
    try:
        json = request.get_json()
        producto = Producto()
        producto.nombre = json['nombre']
        producto.descripcion = json['descripcion']
        producto.precio = json['precio']
        db.session.add(producto)
        db.session.commit()
        return jsonify({"status":200,"mensaje":"Producto"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@approducto.route('/producto/editar',methods=["POST"])
def editarProducto():
    try:
        json = request.get_json()
        producto = Producto.query.get_or_404(json["id"])
        producto.nombre = json['nombre']
        producto.descripcion = json['descripcion']
        producto.precio = json['precio']
        db.session.commit()
        return jsonify({"status":200,"mensaje":"Producto modificar"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@approducto.route('/producto/eliminar',methods=["POST"])
def eliminarProducto():
    try:
        json = request.get_json()
        producto = Producto.query.get_or_404(json["id"])
        db.session.delete(producto)
        db.session.commit()
        return jsonify({"status":200,"mensaje":"Producto al eliminar"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})
    
@approducto.route('/producto/obtener',methods=["POST"])
def obtenerProducto():
    try:
        productos = Producto.query.all()
        listaProductos = []
        for p in productos:
                productox = {}
                productox["nombre"] = p.nombre
                productox["precio"] = p.precio
                productox["descripcion"] = p.descripcion
                listaProductos.append(productox)
        return jsonify({"producto":listaProductos})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})