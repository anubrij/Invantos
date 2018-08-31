from invapi.model.user import user , user_dto
from flask import request
from flask_restplus import Resource

api = user_dto.api
_user = user_dto.user

@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, public_id):
        """get a user given its identifier"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user

