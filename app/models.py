# -*- coding: utf-8 -*-
from app import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(50), nullable=False)
    content =  db.Column(db.String(500), unique = True, nullable=False)
    img_url = db.Column(db.String(30), unique = True, nullable=True)
    date_posted = db.Column(db.DateTime)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname =  db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(200), nullable=False)
    date_send = db.Column(db.DateTime)
