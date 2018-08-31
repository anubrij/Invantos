
from pyodbc import *

cnxn = None #connect('DRIVER={SQL Server};SERVER=anubrij-pc\sql17;DATABASE=invdb;UID=sa;PWD=Qwer1234')
cursor = None #cnxn.cursor()
__path__ = None
def writeclass(tablename):
    print(f"writting class {tablename} to {__path__}")
    file = open(__path__ + "/" + tablename + ".py" , 'w')
    print(__path__ + "/" + tablename + ".py")
    file.truncate()
    file.write("from invapi.dbutil.base import *\n")
    file.write("from flask_restplus import Namespace, fields\n")
    sql = (f"""select TABLE_NAME , COLUMN_NAME , IS_NULLABLE , DATA_TYPE  ,
                            CHARACTER_MAXIMUM_LENGTH , NUMERIC_PRECISION
                            from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = '{tablename}'""")
    columns = cursor.execute(sql).fetchall()
    indent1 = 4 * " "
    indent2 = 8 * " "
    #Model class defination
    modelClass = f"class {tablename}(DbObject):\n"
    modelClass += f"{indent1}def __init__(self , *args, **kwargs):\n"
    modelClass += f"{indent2}super({tablename} , self).__init__(*args, **kwargs)\n"
    modelClass += "{0}"
    #DTO Class defination
    modelClass += f"class {tablename}_dto:\n"
    modelClass += f"#dto class for {tablename}\n"
    modelClass += f"{indent1}api = Namespace('{tablename}' , description='All the operations related to {tablename}')\n"
    modelClass += f"{indent1}{tablename} = api.model('{tablename}' "
    modelClass += ", {1}) \n\n"
    modelDef = ""
    dtoDef = ""
    dtoDef += " {\n"
    for col in columns:
        param = "required=" + ("True" if col[2] == "NO" else "False") + ", type='" + col[3] + "', length=" + (str(col[4]) if col[4] != None else str(col[5]))
        dtoParam = "required=" + ("True" if col[2] == "NO" else "False") + ", description = 'model column'"
        modelDef += f"{indent1}@property\n"
        modelDef += f"{indent1}def {col[1]}(self):\n"
        modelDef += f"{indent2}return self.__{col[1]}__\n"
        modelDef += f"{indent1}@{col[1]}.setter\n"
        modelDef += f"{indent1}@DataMember({param})\n"
        modelDef += f"{indent1}def {col[1]}(self , value):\n"
        modelDef += f"{indent2}self.__{col[1]}__ = value\n"

        dtoDef += f"{indent2}{indent2}'{col[1]}' : fields.String({dtoParam})" + ("," if columns.index(col) != len(columns) - 1 else "") + "\n"
    dtoDef += f"{indent2}{indent2}"
    dtoDef += " }"
    file.write(modelClass.format(modelDef , dtoDef))
    file.close()

def generate(path):
    global __path__
    __path__ = path
    global cnxn
    cnxn = connect('DRIVER={SQL Server};SERVER=anubrij-pc\sql17;DATABASE=invdb;UID=sa;PWD=Qwer1234')
    global cursor
    cursor = cnxn.cursor()

    cursor.execute("select * from INFORMATION_SCHEMA.TABLES where TABLE_NAME <> 'sysdiagrams' ")
    tables = cursor.fetchall()
    for row in tables:
        writeclass(row[2])
    cursor.close()
    cnxn.close()
