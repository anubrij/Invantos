from invapi.dbutil.base import *
from flask_restplus import Namespace, fields
class product(DbObject):
    def __init__(self):
        super(product , self)
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
    @DataMember(required=True, type='nvarchar', length=150)
    def name(self , value):
        self.__name__ = value
    @property
    def brand_id(self):
        return self.__brand_id__
    @brand_id.setter
    @DataMember(required=True, type='numeric', length=18)
    def brand_id(self , value):
        self.__brand_id__ = value
    @property
    def serial(self):
        return self.__serial__
    @serial.setter
    @DataMember(required=False, type='nvarchar', length=200)
    def serial(self , value):
        self.__serial__ = value
    @property
    def batch(self):
        return self.__batch__
    @batch.setter
    @DataMember(required=False, type='nvarchar', length=100)
    def batch(self , value):
        self.__batch__ = value
    @property
    def category_id(self):
        return self.__category_id__
    @category_id.setter
    @DataMember(required=False, type='numeric', length=18)
    def category_id(self , value):
        self.__category_id__ = value
    @property
    def unit_id(self):
        return self.__unit_id__
    @unit_id.setter
    @DataMember(required=False, type='numeric', length=18)
    def unit_id(self , value):
        self.__unit_id__ = value
    @property
    def gst_group_id(self):
        return self.__gst_group_id__
    @gst_group_id.setter
    @DataMember(required=False, type='numeric', length=18)
    def gst_group_id(self , value):
        self.__gst_group_id__ = value
    @property
    def disc_group_id(self):
        return self.__disc_group_id__
    @disc_group_id.setter
    @DataMember(required=False, type='numeric', length=18)
    def disc_group_id(self , value):
        self.__disc_group_id__ = value
    @property
    def saleprice(self):
        return self.__saleprice__
    @saleprice.setter
    @DataMember(required=False, type='numeric', length=18)
    def saleprice(self , value):
        self.__saleprice__ = value
    @property
    def purchaseprice(self):
        return self.__purchaseprice__
    @purchaseprice.setter
    @DataMember(required=False, type='numeric', length=18)
    def purchaseprice(self , value):
        self.__purchaseprice__ = value
    @property
    def sale_constraint_id(self):
        return self.__sale_constraint_id__
    @sale_constraint_id.setter
    @DataMember(required=False, type='numeric', length=18)
    def sale_constraint_id(self , value):
        self.__sale_constraint_id__ = value
    @property
    def barcode(self):
        return self.__barcode__
    @barcode.setter
    @DataMember(required=False, type='nvarchar', length=200)
    def barcode(self , value):
        self.__barcode__ = value
    @property
    def special_text(self):
        return self.__special_text__
    @special_text.setter
    @DataMember(required=False, type='nvarchar', length=200)
    def special_text(self , value):
        self.__special_text__ = value
class product_dto:
#dto class for product
    api = Namespace('product' , description='All the operations related to product')
    product = api.model('product' ,  {
                'id' : fields.String(required=True, description = 'model column'),
                'code' : fields.String(required=True, description = 'model column'),
                'name' : fields.String(required=True, description = 'model column'),
                'brand_id' : fields.String(required=True, description = 'model column'),
                'serial' : fields.String(required=False, description = 'model column'),
                'batch' : fields.String(required=False, description = 'model column'),
                'category_id' : fields.String(required=False, description = 'model column'),
                'unit_id' : fields.String(required=False, description = 'model column'),
                'gst_group_id' : fields.String(required=False, description = 'model column'),
                'disc_group_id' : fields.String(required=False, description = 'model column'),
                'saleprice' : fields.String(required=False, description = 'model column'),
                'purchaseprice' : fields.String(required=False, description = 'model column'),
                'sale_constraint_id' : fields.String(required=False, description = 'model column'),
                'barcode' : fields.String(required=False, description = 'model column'),
                'special_text' : fields.String(required=False, description = 'model column')
                 }) 

