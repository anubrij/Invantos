from invapi.dbutil.base import *
from flask_restplus import Namespace, fields
class Companyuser(DbObject):
    def __init__(self , *args, **kwargs):
        super(Companyuser , self).__init__(*args, **kwargs)
    @property
    def companyid(self):
        return self.__companyid__
    @companyid.setter
    @DataMember(required=True, type='numeric', length=18)
    def companyid(self , value):
        self.__companyid__ = value
    @property
    def userid(self):
        return self.__userid__
    @userid.setter
    @DataMember(required=True, type='numeric', length=18)
    def userid(self , value):
        self.__userid__ = value
class Companyuser_dto:
#dto class for Companyuser
    api = Namespace('Companyuser' , description='All the operations related to Companyuser')
    Companyuser = api.model('Companyuser' ,  {
                        'companyid' : fields.String(required=True, description = 'model column'),
                        'userid' : fields.String(required=True, description = 'model column')
                 }) 

