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
