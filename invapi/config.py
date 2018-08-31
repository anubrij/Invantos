#connection = {"server" : "" , "database" : "" , "user" : "" , "password" : ""}

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class DevConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'ThisIsTheSecretKey1234!')
    DEBUG = False
    AppSetting = {
            "DSN" : "DRIVER={SQL Server};SERVER=anubrij-pc\sql17;DATABASE=invdb;UID=sa;PWD=Qwer1234"
        }
class ProdConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'ThisIsTheSecretKey1234!')
    DEBUG = False
    AppSetting = {
            "DSN" : "DRIVER={SQL Server};SERVER=anubrij-pc\sql17;DATABASE=invdb;UID=sa;PWD=Qwer1234"
        }

ConfigName = dict( 
        dev = DevConfig,
        prod = ProdConfig
    )


