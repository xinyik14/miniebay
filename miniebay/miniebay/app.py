from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    pass

@app.route("/users", methods=['GET', 'POST'])
def list_users():
    pass

@app.route("/users/<username>", methods=['GET', 'POST', 'DELETE'])
def user_by_name(username):
    pass

@app.route("/products", methods=['GET'])
def list_products():
    pass

@app.route("products/<product_id>", methods=['GET', 'POST'])
def product_by_id(product_id):
    pass

@app.route("/users/<username>/products", methods=['GET'])
def list_user_products():
    pass
