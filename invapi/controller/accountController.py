from invapi.model.user import user , user_dto
from flask import request
from flask_restplus import Resource
import time
import json
api = user_dto.api
_user = user_dto.user
users = []
@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        return users

    @api.expect(_user, validate=True)
    #@api.marshal_with(_user)
    def post(self):
        """Creates a new User """
        data = request.json
        u = user(**data)
        users.append(u)
        return "User created successfully"


@api.route('/<id>')
@api.param('id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, public_id):
        """get a user given its identifier"""
        __user = [u for u in users if u.id == id]
        if len(__user) == 0:
            api.abort(404)
        else:
            return __user[0].getResponse()
