from flask import Flask, render_template, url_for
from config import *

app = Flask(__name__)


# Tmp placement for this data, will be pulled from db in the future:
projects = [
    {
        'title': 'Tytuł projektu 1',
        'content': 'opis projektu 1',
        'img_url': 'static/tmp_img.jpg',
        'date_posted': 'Miesiac 20, 2020'
    },
    {
        'title': 'Tytuł projektu 1',
        'content': 'opis projektu 2',
        'img_url': 'static/tmp_img.jpg',
        'date_posted': 'Miesiac 21, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/blog")
def blog():
    return render_template('blog.html', title='My Programming Blog')


@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html', title='My Portfolio', projects=projects)


@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')


if __name__ == '__main__':
    app.run(debug=True)