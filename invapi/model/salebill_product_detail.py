from invapi.dbutil.base import *
from flask_restplus import Namespace, fields
class salebill_product_detail(DbObject):
    def __init__(self):
        super(salebill_product_detail , self)
    @property
    def bill_id(self):
        return self.__bill_id__
    @bill_id.setter
    @DataMember(required=True, type='numeric', length=18)
    def bill_id(self , value):
        self.__bill_id__ = value
    @property
    def product_id(self):
        return self.__product_id__
    @product_id.setter
    @DataMember(required=True, type='numeric', length=18)
    def product_id(self , value):
        self.__product_id__ = value
    @property
    def product_orig_price(self):
        return self.__product_orig_price__
    @product_orig_price.setter
    @DataMember(required=False, type='numeric', length=18)
    def product_orig_price(self , value):
        self.__product_orig_price__ = value
    @property
    def sale_price(self):
        return self.__sale_price__
    @sale_price.setter
    @DataMember(required=True, type='numeric', length=18)
    def sale_price(self , value):
        self.__sale_price__ = value
    @property
    def disc(self):
        return self.__disc__
    @disc.setter
    @DataMember(required=False, type='numeric', length=5)
    def disc(self , value):
        self.__disc__ = value
    @property
    def quantity(self):
        return self.__quantity__
    @quantity.setter
    @DataMember(required=True, type='numeric', length=18)
    def quantity(self , value):
        self.__quantity__ = value
    @property
    def tax(self):
        return self.__tax__
    @tax.setter
    @DataMember(required=False, type='numeric', length=5)
    def tax(self , value):
        self.__tax__ = value
    @property
    def sgst(self):
        return self.__sgst__
    @sgst.setter
    @DataMember(required=False, type='numeric', length=5)
    def sgst(self , value):
        self.__sgst__ = value
    @property
    def cgst(self):
        return self.__cgst__
    @cgst.setter
    @DataMember(required=False, type='numeric', length=5)
    def cgst(self , value):
        self.__cgst__ = value
    @property
    def finalprice(self):
        return self.__finalprice__
    @finalprice.setter
    @DataMember(required=True, type='numeric', length=18)
    def finalprice(self , value):
        self.__finalprice__ = value
class salebill_product_detail_dto:
#dto class for salebill_product_detail
    api = Namespace('salebill_product_detail' , description='All the operations related to salebill_product_detail')
    salebill_product_detail = api.model('salebill_product_detail' ,  {
                'bill_id' : fields.String(required=True, description = 'model column'),
                'product_id' : fields.String(required=True, description = 'model column'),
                'product_orig_price' : fields.String(required=False, description = 'model column'),
                'sale_price' : fields.String(required=True, description = 'model column'),
                'disc' : fields.String(required=False, description = 'model column'),
                'quantity' : fields.String(required=True, description = 'model column'),
                'tax' : fields.String(required=False, description = 'model column'),
                'sgst' : fields.String(required=False, description = 'model column'),
                'cgst' : fields.String(required=False, description = 'model column'),
                'finalprice' : fields.String(required=True, description = 'model column')
                 }) 

