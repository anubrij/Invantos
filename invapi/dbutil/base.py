class DataMember():
    """
    DataMember decorator for model property of model classsself.
    @parameters: required : bool , type : string , length : int
    Example : @DataMember(required = True , length = 10 , type = "decimal")
    """
    def __init__(self, **args):
        self.default = {"required" : False , "type" : "string" , "length": -1}
        self.default.update(args)
    def __call__(self , func):
        def validate(obj , value):
            if(hasattr(type(obj) , "__dbattr__") == False):
                type(obj).__dbattr__ = {}
            type(obj).__dbattr__[func.__name__] = self.default
            if self.default["required"] == True and (value == None or "" + value == ""):
                raise ValueError("Required field")
            if self.default["length"] > -1 and len(str(value)) > self.default["length"]:
                raise ValueError("Length of value can not be greater than " + str(self.default["length"]))
            func(obj , value)
        validate.__dbattr__ = self.default
        return validate


class DbObject(object):
    def __init__(self):
        super(self)
    def getInsert(self):
        return "insert into {0} ({1}) values ({2})".format()

    def create(self):
        pass
    def update(self):
        pass
    def read(id):
        pass
    def delete(self, id):
        pass

class person(DbObject):

    def __init__(self):
        super(person , self)

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
