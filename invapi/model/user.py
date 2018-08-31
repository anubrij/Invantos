from invapi.dbutil.base import *
from flask_restplus import Namespace, fields
class user(DbObject):
    def __init__(self , *args, **kwargs):
        super().__init__(*args, **kwargs)
    @property
    def id(self):
        return self.__id__
    @id.setter
    @DataMember(required=True, type='numeric', length=18)
    def id(self , value):
        self.__id__ = value
    @property
    def username(self):
        return self.__username__
    @username.setter
    @DataMember(required=True, type='nvarchar', length=50)
    def username(self , value):
        self.__username__ = value
    @property
    def firstname(self):
        return self.__firstname__
    @firstname.setter
    @DataMember(required=True, type='nvarchar', length=50)
    def firstname(self , value):
        self.__firstname__ = value
    @property
    def lastname(self):
        return self.__lastname__
    @lastname.setter
    @DataMember(required=False, type='nvarchar', length=50)
    def lastname(self , value):
        self.__lastname__ = value
    @property
    def email(self):
        return self.__email__
    @email.setter
    @DataMember(required=False, type='nvarchar', length=100)
    def email(self , value):
        self.__email__ = value
class user_dto:
#dto class for user
    api = Namespace('user' , description='All the operations related to user')
    user = api.model('user' ,  {
                'id' : fields.String(required=True, description = 'model column'),
                'username' : fields.String(required=True, description = 'model column'),
                'firstname' : fields.String(required=True, description = 'model column'),
                'lastname' : fields.String(required=False, description = 'model column'),
                'email' : fields.String(required=False, description = 'model column')
                 })
