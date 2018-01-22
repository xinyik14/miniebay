from flask_marshmallow import Schema

class UserSchema(Schema):
    class Meta:
        fields = ('id', 'username', 'firstname', 'lastname')

class ProductSchema(Schema):
    class Meta:
        fields = ('id', 'user_id', 'name', 'description', 'price')

user_schema = UserSchema()
users_schema = UserSchema(many=True)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
