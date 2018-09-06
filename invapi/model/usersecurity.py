from invapi.dbutil.base import *
from flask_restplus import Namespace, fields
class Usersecurity(DbObject):
    def __init__(self , *args, **kwargs):
        super(Usersecurity , self).__init__(*args, **kwargs)
    @property
    def userid(self):
        return self.__userid__
    @userid.setter
    @DataMember(required=True, type='numeric', length=18)
    def userid(self , value):
        self.__userid__ = value
    @property
    def password(self):
        return self.__password__
    @password.setter
    @DataMember(required=True, type='nvarchar', length=200)
    def password(self , value):
        self.__password__ = value
    @property
    def secattr1(self):
        return self.__secattr1__
    @secattr1.setter
    @DataMember(required=False, type='nvarchar', length=200)
    def secattr1(self , value):
        self.__secattr1__ = value
    @property
    def secattr2(self):
        return self.__secattr2__
    @secattr2.setter
    @DataMember(required=False, type='nvarchar', length=200)
    def secattr2(self , value):
        self.__secattr2__ = value
    @property
    def secattr3(self):
        return self.__secattr3__
    @secattr3.setter
    @DataMember(required=False, type='nvarchar', length=200)
    def secattr3(self , value):
        self.__secattr3__ = value
    @property
    def date(self):
        return self.__date__
    @date.setter
    @DataMember(required=True, type='datetime', length=None)
    def date(self , value):
        self.__date__ = value
class Usersecurity_dto:
#dto class for Usersecurity
    api = Namespace('Usersecurity' , description='All the operations related to Usersecurity')
    Usersecurity = api.model('Usersecurity' ,  {
                        'userid' : fields.String(required=True, description = 'model column'),
                        'password' : fields.String(required=True, description = 'model column'),
                        'secattr1' : fields.String(required=False, description = 'model column'),
                        'secattr2' : fields.String(required=False, description = 'model column'),
                        'secattr3' : fields.String(required=False, description = 'model column'),
                        'date' : fields.String(required=True, description = 'model column')
                 }) 

