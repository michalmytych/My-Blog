from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from config import *
from flask.views import MethodView



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

app.config['FLASK_ADMIN_SWATCH'] = 'slate'

admin = Admin(app, name='my_blog', template_mode='bootstrap3')
# admin.add_view(ModelView(Post, db.session))


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



class PostsAPI(MethodView):

    def GET(self):
        return "To jest post!"

    def POST(self):
        return 0

    def PUT(self):
        return 0

    def DELETE(self):
        return 0
    

app.add_url_rule('/posts', view_func=PostsAPI.as_view('post'))



if __name__ == '__main__':
    app.run(debug=True)