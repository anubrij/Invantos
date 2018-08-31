import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from invapi.dbutil.modelgenerator import generate
from invapi import InitApp , blueprint

app = InitApp(os.getenv('INVANTOS_ENV') or 'dev')

app.register_blueprint(blueprint)
app.app_context().push()
manager = Manager(app)

@manager.command
def run():
    app.run()

@manager.command
def buildmodel():
     generate("invapi/model")

if __name__ == '__main__':
    manager.run()