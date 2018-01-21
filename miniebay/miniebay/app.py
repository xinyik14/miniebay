from flask import Flask, jsonify, abort, request
import json
app = Flask(__name__)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import User, Product
#app.config.from_object('miniebay.default_settings')
#app.config.from_envvar('ENVFILE')
engine = create_engine('mysql://root:test@127.0.0.1/miniebay')
Session = sessionmaker(bind=engine)

@app.route("/")
def index():
    return "hello world"

@app.route("/users", methods=['GET', 'POST'])
def list_users():
    if request.method == 'GET':
        session = Session()
        return jsonify([u.to_json() for u in
                        session.query(User).limit(100).all()])

@app.route("/users/<username>", methods=['GET', 'PUT', 'DELETE'])
def user_by_name(username):
    if request.method == 'GET':
        session = Session()
        user = session.query(User).filter(User.username==username).one_or_none()
        if user is None:
            abort(404)
        else:
            return jsonify(user.to_json())


@app.route("/products", methods=['GET', 'POST'])
def list_products():
    if request.method == 'GET':
        session = Session()
        return jsonify([p.to_json() for p in
                            session.query(Product).limit(100).all()])
    elif request.method == 'POST':
        session = Session()
        session.commit()

@app.route("/products/<product_id>", methods=['GET', 'PUT'])
def product_by_id(product_id):
    if request.method == 'GET':
        session = Session()
        product = session.query(User).filter(Product.id==id).one_or_none()
        if user is None:
            abort(404)
        else:
            return jsonify(user.to_json())

@app.route("/users/<user_id>/products", methods=['GET'])
def list_user_products(user_id):
    session = Session()
    return jsonify([p.to_json() for p in
                    session.query(Product).filter(Product.user_id==user_id).limit(100).all()])
