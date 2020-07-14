# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import os


basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config['SECRET_KEY'] = '************'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)
mail = Mail(app)


app.config['FLASK_ADMIN_SWATCH'] = 'slate'


app.config.from_object(__name__)


from app import views
from app import admin_views
from app import error_handlers