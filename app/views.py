from app import app, db
from flask import render_template, url_for



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