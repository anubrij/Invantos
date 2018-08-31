from invapi.dbutil.base import *
from flask_restplus import Namespace, fields
class companyuser(DbObject):
    def __init__(self , *args, **kwargs):
        super(companyuser , self).__init__(*args, **kwargs)
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
class companyuser_dto:
#dto class for companyuser
    api = Namespace('companyuser' , description='All the operations related to companyuser')
    companyuser = api.model('companyuser' ,  {
                'companyid' : fields.String(required=True, description = 'model column'),
                'userid' : fields.String(required=True, description = 'model column')
                 }) 

