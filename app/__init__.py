from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from config import *
import os

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Tmp placement for this data, will be pulled from db in the future:
# This temporary model for development period

base_title = "Michał Mytych"
mail = "m****************m"
github_link = "https://github.com/michalmytych"


posts = [
    {
        'title': 'Tytuł postu 1',
        'author': 'Michał Mytych',
        'content': 'Tresc postu nr 1',
        'img_url': 'static/tmp_img.jpg',
        'date_posted': 'Miesiac 20, 2020'
    },
    {
        'title': 'Tytuł postu 2',
        'author': 'Michał Mytych',
        'content': 'Tresc postu nr 2',
        'img_url': 'static/tmp_img.jpg',
        'date_posted': 'Miesiac 20, 2020'
    },    {
        'title': 'Tytuł postu 2',
        'author': 'Michał Mytych',
        'content': 'Tresc postu nr 2',
        'img_url': 'static/tmp_img.jpg',
        'date_posted': 'Miesiac 20, 2020'
    }
]
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config['SECRET_KEY'] = '************'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)


app.config['FLASK_ADMIN_SWATCH'] = 'slate'
admin = Admin(app, name='my_blog', template_mode='bootstrap3')


app.config.from_object(__name__)
from app import views