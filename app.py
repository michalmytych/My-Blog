from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from config import *



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/c/users/micha/source/repos/MyBlogAndPortfolio\My-Portfolio-and-Blog/my_blog_data.db'

db = SQLAlchemy(app)

app.config['FLASK_ADMIN_SWATCH'] = 'slate'

admin = Admin(app, name='my_blog', template_mode='bootstrap3')




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




@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/blog")
def blog():
    return render_template(
        'blog.html', 
        title='My Programming Blog',
        posts=posts)


@app.route("/contact")
def contact():
    return render_template(
        'contact.html', 
        title='Contact',
        github_link=github_link,
        mail=mail)


if __name__ == '__main__':
    app.run(debug=True)