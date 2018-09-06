import pyodbc
import itertools
import inspect

class DbType(object):
    def nvarchar(length=50):
        return "nvarchar({0})".format(length)
    def varchar(length=50):
        return "varchar({0})".format(length)
    def bigint():
        return "bigint"
    def bit():
        return "bit"
    def numeric(precision , scale):
        return "numeric({0} , {1})".format(precision , scale)
    def date():
        return "date"
    def datetime():
        return "datetime"

class iQuery:
    def __init__(self , TEntity):
        self.__fields__ = inspect.getmembers(TEntity , lambda o: isinstance(o, property))
        self.__sql__ = []
        self.__where__ = False
    @property
    def Select(self):
        self.__sql__ = []
        self.__sql__ += ["SELECT"]
        self.__sql__ += [" " + f[0] for f in  self.__fields__] 
        self.__sql__ += ["FROM"]
        self.__sql__ += [self.__type__.__name__.upper()]
        return self
    def Where(self, **kwargs):
        self.__sql__ +=  ["WHERE"] if not self.__where__ else ["AND"]
        self.__sql__ += [" (" + " AND ".join([f + '=' + str(kwargs[f]) for f in kwargs]) + ") "]
        return self
    def Or(self , **kwargs):
        self.__sql__ +=  ["OR"]
        self.__sql__ +=  self.__sql__ += [" (" + " OR ".join([f + '=' + str(kwargs[f]) for f in kwargs]) + ") "]
        return self
    def OrderBy(self , *args , **kwargs):
        pass
    def getAll(self):
        return "\n".join(self.__sql__)
    def getOne(self):
        pass
    def getLast(self):
        pass

class Table(iQuery):
    def __init__(self, TEntity):
        super(self.__class__ , self).__init__(TEntity)
        if type(TEntity).__name__ != "type":
            raise TypeError("expected type as parameter")
        self.__type__ = TEntity

    def __validate(self, entity):
        if entity == None:
            raise ValueError("value can not be none")
        if type(entity).__name__ != self.__type__.__name__:
            raise TypeError("expected type is " + self.__type__.__name__)

    def Add(self, entity):
        self.__validate(entity)
        if hasattr(self , "collection"):
           self.collection.append(entity)
        else:
           self.collection = []
           self.collection.append(entity)

    def AddRange(self , entities):
        for entity in entities:
            self.__validate(entity)
        for entity in entities:
            self.Add(entity)


class DbContext(object):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)


    




