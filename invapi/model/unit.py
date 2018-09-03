from invapi.dbutil.base import *
from flask_restplus import Namespace, fields
class unit(DbObject):
    def __init__(self , *args, **kwargs):
        super(unit , self).__init__(*args, **kwargs)
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
class unit_dto:
#dto class for unit
    api = Namespace('unit' , description='All the operations related to unit')
    unit = api.model('unit' ,  {
                        'id' : fields.String(required=True, description = 'model column'),
                        'name' : fields.String(required=True, description = 'model column')
                 }) 

