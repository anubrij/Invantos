from base import *
class company(DbObject):

    def __init__(self):
        super(company , self)

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
    def country_code(self):
        return self.__country_code__

    @country_code.setter
    @DataMember(required=True, type='nvarchar', length=50)
    def country_code(self , value):
        self.__country_code__ = value

    @property
    def state_code(self):
        return self.__state_code__

    @state_code.setter
    @DataMember(required=False, type='nvarchar', length=50)
    def state_code(self , value):
        self.__state_code__ = value

    @property
    def city(self):
        return self.__city__

    @city.setter
    @DataMember(required=False, type='nvarchar', length=100)
    def city(self , value):
        self.__city__ = value

    @property
    def address(self):
        return self.__address__

    @address.setter
    @DataMember(required=False, type='nvarchar', length=500)
    def address(self , value):
        self.__address__ = value

    @property
    def zipcode(self):
        return self.__zipcode__

    @zipcode.setter
    @DataMember(required=False, type='nvarchar', length=50)
    def zipcode(self , value):
        self.__zipcode__ = value

    @property
    def mobile(self):
        return self.__mobile__

    @mobile.setter
    @DataMember(required=False, type='numeric', length=10)
    def mobile(self , value):
        self.__mobile__ = value

    @property
    def licence(self):
        return self.__licence__

    @licence.setter
    @DataMember(required=False, type='nvarchar', length=100)
    def licence(self , value):
        self.__licence__ = value

    @property
    def tan(self):
        return self.__tan__

    @tan.setter
    @DataMember(required=False, type='nvarchar', length=50)
    def tan(self , value):
        self.__tan__ = value

    @property
    def pan(self):
        return self.__pan__

    @pan.setter
    @DataMember(required=False, type='nvarchar', length=50)
    def pan(self , value):
        self.__pan__ = value

    @property
    def tin(self):
        return self.__tin__

    @tin.setter
    @DataMember(required=False, type='nvarchar', length=50)
    def tin(self , value):
        self.__tin__ = value

    @property
    def cst(self):
        return self.__cst__

    @cst.setter
    @DataMember(required=False, type='nvarchar', length=50)
    def cst(self , value):
        self.__cst__ = value

    @property
    def gstin(self):
        return self.__gstin__

    @gstin.setter
    @DataMember(required=False, type='nvarchar', length=50)
    def gstin(self , value):
        self.__gstin__ = value

