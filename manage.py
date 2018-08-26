from flask_script import Manager
from invapi.dbutil.modelgenerator import generate
from invapi import create_app

app = create_app()
manager = Manager(app)


def buildmodel():
    generate("invapi/model")


def runapp():
    app.run()

buildmodel()
