
from pyodbc import *

cnxn = None #connect('DRIVER={SQL Server};SERVER=anubrij-pc\sql17;DATABASE=invdb;UID=sa;PWD=Qwer1234')
cursor = None #cnxn.cursor()
__path__ = None
def writeclass(tablename):
    print(f"writting class {tablename} to {__path__}")
    file = open(__path__ + "/" + tablename + ".py" , 'w')
    print(__path__ + "/" + tablename + ".py")
    file.truncate()
    file.write("from base import *\n")
    sql = (f"""select TABLE_NAME , COLUMN_NAME , IS_NULLABLE , DATA_TYPE  ,
                            CHARACTER_MAXIMUM_LENGTH , NUMERIC_PRECISION
                            from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = '{tablename}'""")
    columns = cursor.execute(sql).fetchall()
    indent1 = 4 * " "
    indent2 = 8 * " "
    file.write(f"class {tablename}(DbObject):\n\n")
    file.write(f"{indent1}def __init__(self):\n")
    file.write(f"{indent2}super({tablename} , self)\n\n")
    for col in columns:
        param = "required=" + ("True" if col[2] == "NO" else "False") + ", type='" + col[3] + "', length=" + (str(col[4]) if col[4] != None else str(col[5]))
        file.write(f"{indent1}@property\n")
        file.write(f"{indent1}def {col[1]}(self):\n")
        file.write(f"{indent2}return self.__{col[1]}__\n\n")
        file.write(f"{indent1}@{col[1]}.setter\n")
        file.write(f"{indent1}@DataMember({param})\n")
        file.write(f"{indent1}def {col[1]}(self , value):\n")
        file.write(f"{indent2}self.__{col[1]}__ = value\n\n")
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
