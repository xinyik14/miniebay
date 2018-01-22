from flask import (
    Flask, 
    Response, 
    abort, 
    jsonify, 
    redirect,
    request 
)
from flask_login import (
    LoginManager, 
    login_required, 
    login_user,
    logout_user
)
from flask_marshmallow import Marshmallow
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import User, Product
from schemas import (
    user_schema,
    users_schema,
    product_schema,
    products_schema
)
import datetime

app = Flask(__name__)
#app.config.from_object('miniebay.default_settings')
#app.config.from_envvar('ENVFILE')
# login manager
app.config.update(
    SECRET_KEY = 'secret_key'
)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

engine = create_engine('mysql://root:test@127.0.0.1/miniebay')
Session = sessionmaker(bind=engine)

@app.route("/")
@login_required
def index():
    return "hello world"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = find_user_by_name(username)
        if user is None:
            return abort(404)
        elif user.password == password:
            login_user(user)
            return redirect(request.args.get("next"))
        else:
            return abort(401)
    else:
        return Response('''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
        ''')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')

def find_user_by_id(id):
    session = Session()
    try:
        return session.query(User).get(id)
    except Exception:
        return None

def find_user_by_name(username):
    session = Session()
    return session.query(User).filter(User.username==username).one_or_none()

@app.route("/api/users", methods=['GET', 'POST'])
def list_users():
    if request.method == 'GET':
        session = Session()
        users = session.query(User).limit(100).all()
        result = users_schema.dump(users)
        return jsonify(result.data)
    else:
        abort(405)

@app.route("/api/users/<id>", methods=['GET', 'PUT', 'DELETE'])
@login_required
def user_detail(id):
    if request.method == 'GET':
        user = find_user_by_id(id)
        if user is None:
            abort(404)
        else:
            result = user_schema.dump(user) 
            return jsonify(result.data)
    else:
        abort(405)

@app.route("/api/products", methods=['GET', 'POST'])
@login_required
def list_products():
    if request.method == 'GET':
        session = Session()
        products = session.query(Product).limit(100).all()
        result = products_schema.dump(products)
        return jsonify(result.data)
    elif request.method == 'POST':
        product_json = request.get_json()
        if not product_json:
            return jsonify({'message': 'No input data provided'}), 400
        data, errors = product_schema.load(product_json)
        if errors:
            return jsonify(errors), 400 
        user = find_user_by_id(data['user_id'])
        if not user:
            return jsonify({'message': 'user does not exist'}), 400
        product = Product(**data)
        session = Session()
        session.add(product)
        session.commit()
        result = product_schema.dump(session.query(Product).get(product.id))
        return jsonify(result.data)
    else:
        abort(405)

@app.route("/api/products/<id>", methods=['GET', 'PUT', 'DELETE'])
@login_required
def product_detail(id):
    if request.method == 'GET':
        product = get_product_by_id(id)
        if product:
            result = product_schema.dump(product) 
            return jsonify(result.data)
        else:
            abort(404)
    elif request.method == 'PUT':
        product = get_product_by_id(id)
        if not product:
            return jsonify({'message': 'Product not exists'}), 404
        product_json = request.get_json()
        if not product_json:
            return jsonify({'message': 'No input data provided'}), 400
        data, errors = product_schema.load(product_json)
        if errors:
            return jsonify(errors), 400 
        if data['user_id'] != getattr(product, 'user_id'):
            return jsonify({'message': 'Only user created the product can update'}), 400
        session = Session()
        session.query(Product).filter(Product.id==id).update(data)
        session.commit()
        product = get_product_by_id(id)
        result = product_schema.dump(product)
        return jsonify(result.data)
    else:
        abort(405)

def get_product_by_id(id):
    session = Session()
    try:
        return session.query(Product).get(id)
    except Exception:
        return None

@app.route("/api/users/<user_id>/products", methods=['GET'])
@login_required
def list_user_products(user_id):
    session = Session()
    products = session.query(Product).filter(Product.user_id==user_id).limit(100).all()
    result = products_schema.dump(products)
    return jsonify(result.data)

@login_manager.user_loader
def load_user(id):
    session = Session()
    return session.query(User).get(id)

# handle login failed
@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')
