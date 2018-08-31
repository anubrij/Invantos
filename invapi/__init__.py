from flask import Flask
from .config import ConfigName

from flask_restplus import Api
from flask import Blueprint
from invapi.controller.accountController import api as accountApi

def InitApp(config_name):
    config = ConfigName[config_name]
    app = Flask(__name__)
    app.config.from_object(config)
    return app

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Invantos api for applications',
          version='1.0',
          description='an invantory system'
          )
api.add_namespace(accountApi)
