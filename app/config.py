# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

"""
Command to change app configuration, for example:
export APP_SETTINGS="config.DevelopmentConfig"

export DATABASE_URL="postgresql://localhost/Posts"

To violently kill app process running on port 5000:
sudo kill -9 $(lsof -t -i:5000)
"""


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ["SECRET_KEY"]
    DATABASE_URL="postgresql://localhost/MyBlog"
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ADMIN_SWATCH = 'slate'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = "guitar.myt@gmail.com"
    MAIL_PASSWORD = ""
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True



base_title = u"Michal Mytych"
mail = u"m****************m"
github_link = u"https://github.com/michalmytych"


posts = [
    {
        'id' : 0,
        'title': u'Tytul posta 1',
        'author': u'Michal Mytych',
        'content': u'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Eaque, laudantium quas! Placeat optio eaque officia, deserunt veniam repellat tempora nulla explicabo at! Consequuntur doloremque quae rem veritatis aut corrupti a.',
        'img_url': u'1.jpg',
        'date_posted': u'Miesiac 20, 2020'
    },
    {
        'id' : 1,
        'title': u'Tytul posta 2',
        'author': u'Michal Mytych',
        'content': u'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Eaque, laudantium quas! Placeat optio eaque officia, deserunt veniam repellat tempora nulla explicabo at! Consequuntur doloremque quae rem veritatis aut corrupti a.',
        'img_url': u'2.jpg',
        'date_posted': u'Miesiac 20, 2020'
    },    
    {
        'id' : 2,
        'title': u'Tytuł posta 2',
        'author': u'Michal Mytych',
        'content': u'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Eaque, laudantium quas! Placeat optio eaque officia, deserunt veniam repellat tempora nulla explicabo at! Consequuntur doloremque quae rem veritatis aut corrupti a.',
        'img_url': u'3.jpg',
        'date_posted': u'Miesiac 20, 2020'
    }
]