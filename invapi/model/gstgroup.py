from invapi.dbutil.base import *
from flask_restplus import Namespace, fields
class Gstgroup(DbObject):
    def __init__(self , *args, **kwargs):
        super(Gstgroup , self).__init__(*args, **kwargs)
    @property
    def id(self):
        return self.__id__
    @id.setter
    @DataMember(required=True, type='numeric', length=18)
    def id(self , value):
        self.__id__ = value
    @property
    def name(self):
        return self.__name__
    @name.setter
    @DataMember(required=True, type='nvarchar', length=50)
    def name(self , value):
        self.__name__ = value
    @property
    def cgst(self):
        return self.__cgst__
    @cgst.setter
    @DataMember(required=False, type='numeric', length=5)
    def cgst(self , value):
        self.__cgst__ = value
    @property
    def sgst(self):
        return self.__sgst__
    @sgst.setter
    @DataMember(required=False, type='numeric', length=5)
    def sgst(self , value):
        self.__sgst__ = value
class Gstgroup_dto:
#dto class for Gstgroup
    api = Namespace('Gstgroup' , description='All the operations related to Gstgroup')
    Gstgroup = api.model('Gstgroup' ,  {
                        'id' : fields.String(required=True, description = 'model column'),
                        'name' : fields.String(required=True, description = 'model column'),
                        'cgst' : fields.String(required=False, description = 'model column'),
                        'sgst' : fields.String(required=False, description = 'model column')
                 }) 

