from base import *
class companyuser(DbObject):

    def __init__(self):
        super(companyuser , self)

    @property
    def companyid(self):
        return self.__companyid__

    @companyid.setter
    @DataMember(required=True, type='numeric', length=18)
    def companyid(self , value):
        self.__companyid__ = value

    @property
    def userid(self):
        return self.__userid__

    @userid.setter
    @DataMember(required=True, type='numeric', length=18)
    def userid(self , value):
        self.__userid__ = value

