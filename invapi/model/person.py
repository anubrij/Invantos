from invapi.dbutil.base import *
from flask_restplus import Namespace, fields
class Person(DbObject):
    def __init__(self , *args, **kwargs):
        super(Person , self).__init__(*args, **kwargs)
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
    @DataMember(required=True, type='nvarchar', length=200)
    def name(self , value):
        self.__name__ = value
    @property
    def address(self):
        return self.__address__
    @address.setter
    @DataMember(required=False, type='nvarchar', length=500)
    def address(self , value):
        self.__address__ = value
    @property
    def mobile(self):
        return self.__mobile__
    @mobile.setter
    @DataMember(required=False, type='nvarchar', length=13)
    def mobile(self , value):
        self.__mobile__ = value
    @property
    def pan(self):
        return self.__pan__
    @pan.setter
    @DataMember(required=False, type='nvarchar', length=10)
    def pan(self , value):
        self.__pan__ = value
    @property
    def adhar(self):
        return self.__adhar__
    @adhar.setter
    @DataMember(required=False, type='numeric', length=18)
    def adhar(self , value):
        self.__adhar__ = value
class Person_dto:
#dto class for Person
    api = Namespace('Person' , description='All the operations related to Person')
    Person = api.model('Person' ,  {
                        'id' : fields.String(required=True, description = 'model column'),
                        'name' : fields.String(required=True, description = 'model column'),
                        'address' : fields.String(required=False, description = 'model column'),
                        'mobile' : fields.String(required=False, description = 'model column'),
                        'pan' : fields.String(required=False, description = 'model column'),
                        'adhar' : fields.String(required=False, description = 'model column')
                 }) 

