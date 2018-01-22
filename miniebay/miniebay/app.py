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

ma = Marshmallow(app)

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

@app.route("/api/users/<id>", methods=['GET', 'PUT', 'DELETE'])
@login_required
def user_detail(id):
    if request.method == 'GET':
        user = find_user_by_id(id)
        if user is None:
            abort(404)
        else:
            return user_schema.jsonify(user) 


@app.route("/api/products", methods=['GET', 'POST'])
def list_products():
    if request.method == 'GET':
        session = Session()
        products = session.query(Product).limit(100).all()
        result = products_schema.dump(products)
        return jsonify(result.data)
    elif request.method == 'POST':
        product_json = request.data
        session = Session()
        session.commit()

@app.route("/api/products/<id>", methods=['GET', 'PUT'])
@login_required
def product_detail(id):
    if request.method == 'GET':
        session = Session()
        product = session.query(User).filter(Product.id==id).one_or_none()
        if product is None:
            abort(404)
        else:
            return product_schema.jsonify(product) 

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
