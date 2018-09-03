from invapi.dbutil.base import *
from flask_restplus import Namespace, fields
class customer(DbObject):
    def __init__(self , *args, **kwargs):
        super(customer , self).__init__(*args, **kwargs)
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
    def address(self):
        return self.__address__
    @address.setter
    @DataMember(required=False, type='nvarchar', length=500)
    def address(self , value):
        self.__address__ = value
    @property
    def city(self):
        return self.__city__
    @city.setter
    @DataMember(required=False, type='nvarchar', length=50)
    def city(self , value):
        self.__city__ = value
    @property
    def state(self):
        return self.__state__
    @state.setter
    @DataMember(required=False, type='nvarchar', length=50)
    def state(self , value):
        self.__state__ = value
    @property
    def country(self):
        return self.__country__
    @country.setter
    @DataMember(required=False, type='nvarchar', length=50)
    def country(self , value):
        self.__country__ = value
    @property
    def mobile(self):
        return self.__mobile__
    @mobile.setter
    @DataMember(required=False, type='nvarchar', length=13)
    def mobile(self , value):
        self.__mobile__ = value
    @property
    def tin(self):
        return self.__tin__
    @tin.setter
    @DataMember(required=False, type='numeric', length=18)
    def tin(self , value):
        self.__tin__ = value
    @property
    def licence(self):
        return self.__licence__
    @licence.setter
    @DataMember(required=False, type='nvarchar', length=50)
    def licence(self , value):
        self.__licence__ = value
    @property
    def gst(self):
        return self.__gst__
    @gst.setter
    @DataMember(required=False, type='nvarchar', length=50)
    def gst(self , value):
        self.__gst__ = value
class customer_dto:
#dto class for customer
    api = Namespace('customer' , description='All the operations related to customer')
    customer = api.model('customer' ,  {
                        'id' : fields.String(required=True, description = 'model column'),
                        'code' : fields.String(required=True, description = 'model column'),
                        'name' : fields.String(required=True, description = 'model column'),
                        'address' : fields.String(required=False, description = 'model column'),
                        'city' : fields.String(required=False, description = 'model column'),
                        'state' : fields.String(required=False, description = 'model column'),
                        'country' : fields.String(required=False, description = 'model column'),
                        'mobile' : fields.String(required=False, description = 'model column'),
                        'tin' : fields.String(required=False, description = 'model column'),
                        'licence' : fields.String(required=False, description = 'model column'),
                        'gst' : fields.String(required=False, description = 'model column')
                 }) 

