from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from config import *


basedir = os.path.abspath(os.path.dirname(__file__))

app.config['FLASK_ADMIN_SWATCH'] = 'slate'

admin = Admin(app, name='my_blog', template_mode='bootstrap3')

app = Flask(__name__)
app.config['SECRET_KEY'] = '************'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)


app.config.from_object(__name__)
from app import views