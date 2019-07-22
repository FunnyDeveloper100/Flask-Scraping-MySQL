from flask_script import Manager
from flask_migrate import MigrateCommand
from app import application


manager = Manager(application)
manager.add_command('db', MigrateCommand)

if __name__ = '__name__':
    manager.run()
