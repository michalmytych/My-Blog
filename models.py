from sqlalchemy import Column, Integer, String, ForeignKey, Date
from flask_appbuilder import Model



class Post(Model):
    id = Column(Integer, primary_key=True)
    author = Column(String(50), nullable=False)
    content =  Column(String(500), unique = True, nullable=False)
    img_url = Column(String(30), unique = True, nullable=True)
    date_posted = Column(Date)

    def __repr__(self):
        return self.name