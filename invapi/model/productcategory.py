from invapi.dbutil.base import *
from flask_restplus import Namespace, fields
class productcategory(DbObject):
    def __init__(self , *args, **kwargs):
        super(productcategory , self).__init__(*args, **kwargs)
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
class productcategory_dto:
#dto class for productcategory
    api = Namespace('productcategory' , description='All the operations related to productcategory')
    productcategory = api.model('productcategory' ,  {
                'id' : fields.String(required=True, description = 'model column'),
                'name' : fields.String(required=True, description = 'model column')
                 }) 

