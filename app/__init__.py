from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
import os


basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config['SECRET_KEY'] = '************'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)


app.config['FLASK_ADMIN_SWATCH'] = 'slate'
admin = Admin(app, name='my_blog', template_mode='bootstrap3')


app.config.from_object(__name__)


from app import views
from app import admin_views