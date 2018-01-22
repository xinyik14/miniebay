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
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import User, Product
import json

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

def find_user_by_name(username):
    session = Session()
    return session.query(User).filter(User.username==username).one_or_none()

@app.route("/users", methods=['GET', 'POST'])
def list_users():
    if request.method == 'GET':
        session = Session()
        return jsonify([u.to_json() for u in
                        session.query(User).limit(100).all()])

@app.route("/users/<username>", methods=['GET', 'PUT', 'DELETE'])
def user_by_name(username):
    if request.method == 'GET':
        user = find_user_by_name(username)
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

@login_manager.user_loader
def load_user(userid):
    session = Session()
    return session.query(User).get(userid)

# handle login failed
@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')
