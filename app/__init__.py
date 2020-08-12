# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from datetime import datetime


load_dotenv(find_dotenv())

app = Flask(__name__)
db = SQLAlchemy(app)
mail = Mail(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_envvar('FLASK_CONFIG')


from app import views
from app import admin_views
from app import error_handlers

from app.models import Post

