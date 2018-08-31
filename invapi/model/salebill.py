from invapi.dbutil.base import *
from flask_restplus import Namespace, fields
class salebill(DbObject):
    def __init__(self):
        super(salebill , self)
    @property
    def id(self):
        return self.__id__
    @id.setter
    @DataMember(required=True, type='numeric', length=18)
    def id(self , value):
        self.__id__ = value
    @property
    def number(self):
        return self.__number__
    @number.setter
    @DataMember(required=True, type='nvarchar', length=50)
    def number(self , value):
        self.__number__ = value
    @property
    def customer_id(self):
        return self.__customer_id__
    @customer_id.setter
    @DataMember(required=True, type='numeric', length=18)
    def customer_id(self , value):
        self.__customer_id__ = value
    @property
    def billdate(self):
        return self.__billdate__
    @billdate.setter
    @DataMember(required=True, type='datetime', length=None)
    def billdate(self , value):
        self.__billdate__ = value
    @property
    def totalitems(self):
        return self.__totalitems__
    @totalitems.setter
    @DataMember(required=False, type='int', length=10)
    def totalitems(self , value):
        self.__totalitems__ = value
    @property
    def totalamount(self):
        return self.__totalamount__
    @totalamount.setter
    @DataMember(required=False, type='numeric', length=18)
    def totalamount(self , value):
        self.__totalamount__ = value
    @property
    def totalprofit(self):
        return self.__totalprofit__
    @totalprofit.setter
    @DataMember(required=False, type='numeric', length=18)
    def totalprofit(self , value):
        self.__totalprofit__ = value
    @property
    def special_disc(self):
        return self.__special_disc__
    @special_disc.setter
    @DataMember(required=False, type='numeric', length=5)
    def special_disc(self , value):
        self.__special_disc__ = value
    @property
    def user_id(self):
        return self.__user_id__
    @user_id.setter
    @DataMember(required=True, type='numeric', length=18)
    def user_id(self , value):
        self.__user_id__ = value
class salebill_dto:
#dto class for salebill
    api = Namespace('salebill' , description='All the operations related to salebill')
    salebill = api.model('salebill' ,  {
                'id' : fields.String(required=True, description = 'model column'),
                'number' : fields.String(required=True, description = 'model column'),
                'customer_id' : fields.String(required=True, description = 'model column'),
                'billdate' : fields.String(required=True, description = 'model column'),
                'totalitems' : fields.String(required=False, description = 'model column'),
                'totalamount' : fields.String(required=False, description = 'model column'),
                'totalprofit' : fields.String(required=False, description = 'model column'),
                'special_disc' : fields.String(required=False, description = 'model column'),
                'user_id' : fields.String(required=True, description = 'model column')
                 }) 

