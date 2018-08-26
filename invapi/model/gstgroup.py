from base import *
class gstgroup(DbObject):

    def __init__(self):
        super(gstgroup , self)

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

