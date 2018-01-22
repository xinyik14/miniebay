from marshmallow import Schema, pre_load, fields, validate

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, 
                          validate=validate.Email(error='Not a valid email address'))
    password = fields.Str(required=True, 
                          load_only=True, 
                          validate=[validate.Length(min=6, max=18)])
    firstname = fields.Str(validate=[validate.Length(max=64)])
    lastname = fields.Str(validate=[validate.Length(max=64)])

    @pre_load
    def process_input(self, data):
        data['username'] = data['username'].lower().strip()
        return data

class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    name = fields.Str(required=True, 
                      validate=[validate.Length(max=100, 
                                                error='name must be within 100 characters')])
    description = fields.Str()
    price = fields.Float(validate=[validate.Range(min=0, 
                                                  error='price must be positive')])

user_schema = UserSchema()
users_schema = UserSchema(many=True)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
