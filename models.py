from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from flask_appbuilder import Model



class Post(Model):
    id = Column(Integer, primary_key=True)
    author = Column(String(50), nullable=False)
    content =  Column(String(500), unique = True, nullable=False)
    img_url = Column(String(30), unique = True, nullable=True)
    date_posted = Column(DateTime)


class Contact(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname =  Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    message = Column(String(200), nullable=False)
    date_send = Column(DateTime)



"""class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(21), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    tagline = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    img_file = db.Column(db.String(12), nullable=True)"""