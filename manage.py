#!bin/python

from app import app
from flask.ext.script import Manager
from flask.ext.migrate import MigrateCommand

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def hello():
    print("hello")

if __name__ == "__main__":
    manager.run()
