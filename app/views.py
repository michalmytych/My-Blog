from app import app, db
from flask import render_template, url_for


# * * * * * * * * * * * * * * * * * * 
from app.config import posts, base_title, mail, github_link
# * * * * * * * * * * * * * * * * * * 



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