from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db

"""
To create database, being in My-Blog direction run commands:
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
or python3 ...
"""

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
