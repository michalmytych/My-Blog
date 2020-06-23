from app import app, db
from flask import render_template, url_for, request, redirect


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


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        contact_request = request.form

        # maybe add some id and client side datetime
        name = contact_request["name"]
        surname = contact_request["surname"]

        # maybe make email required
        email = contact_request["email"]
        message = contact_request["message"]
        
        
        print(contact_request)

        return redirect(request.url)


    return render_template(
        'contact.html', 
        title='Contact',
        github_link=github_link,
        mail=mail)


if __name__ == '__main__':
    app.run(debug=True)