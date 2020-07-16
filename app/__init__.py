# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import os
from datetime import datetime


basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config['SECRET_KEY'] = '************'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
mail = Mail(app)


app.config['FLASK_ADMIN_SWATCH'] = 'slate'


app.config.from_object(__name__)


from app import views
from app import admin_views
from app import error_handlers


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(50), unique = True, nullable=False)
    content =  db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(30), unique = True, nullable=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    thumbs_up = db.Column(db.Integer, default=0, nullable=True)
    thumbs_down = db.Column(db.Integer, default=0, nullable=True)

    def __repr__(self):
        return f"Post(id:{self.id}, title:{self.title}"