from flask import Flask, render_template, url_for
from config import *

app = Flask(__name__)



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/blog")
def blog():
    return render_template('blog.html', title='My Programming Blog')


@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html', title='My Portfolio')


@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')


if __name__ == '__main__':
    app.run(debug=True)