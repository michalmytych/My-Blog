from app import db
from datetime import datetime


class Post(db.Model):
    __tablename__ = 'Posts'

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(50), unique = True, nullable=False)
    content =  db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(30), unique = True, nullable=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Post(id:{self.id}, title:{self.title}"

    def serialize(self):
        return {
            'id': self.id, 
            'author': self.author,
            'title': self.title,
            'content': self.content,
            'img_url': self.img_url,
            'date_posted' : self.date_posted
        }