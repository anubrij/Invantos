from base import *
class productbrand(DbObject):

    def __init__(self):
        super(productbrand , self)

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

