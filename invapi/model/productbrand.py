from invapi.dbutil.base import *
from flask_restplus import Namespace, fields
class productbrand(DbObject):
    def __init__(self , *args, **kwargs):
        super(productbrand , self).__init__(*args, **kwargs)
    @property
    def id(self):
        return self.__id__
    @id.setter
    @DataMember(required=True, type='numeric', length=18)
    def id(self , value):
        self.__id__ = value
    @property
    def code(self):
        return self.__code__
    @code.setter
    @DataMember(required=True, type='nvarchar', length=50)
    def code(self , value):
        self.__code__ = value
    @property
    def name(self):
        return self.__name__
    @name.setter
    @DataMember(required=True, type='nvarchar', length=200)
    def name(self , value):
        self.__name__ = value
    @property
    def mr_person_id(self):
        return self.__mr_person_id__
    @mr_person_id.setter
    @DataMember(required=True, type='numeric', length=18)
    def mr_person_id(self , value):
        self.__mr_person_id__ = value
class productbrand_dto:
#dto class for productbrand
    api = Namespace('productbrand' , description='All the operations related to productbrand')
    productbrand = api.model('productbrand' ,  {
                        'id' : fields.String(required=True, description = 'model column'),
                        'code' : fields.String(required=True, description = 'model column'),
                        'name' : fields.String(required=True, description = 'model column'),
                        'mr_person_id' : fields.String(required=True, description = 'model column')
                 }) 

