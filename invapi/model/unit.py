from base import *
class unit(DbObject):

    def __init__(self):
        super(unit , self)

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

