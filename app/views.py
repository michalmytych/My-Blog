# -*- coding: utf-8 -*-

from app import app, db
from flask import render_template, url_for, request, redirect, abort
from app.config import posts, base_title, mail, github_link


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

        # Here data from contact form will be 
        # prepared to be send as an email to admin

        return render_template(
            'message_sent.html', 
            title='Contact',
            github_link=github_link,
            mail=mail)


    return render_template(
        'contact.html', 
        title='Contact',
        github_link=github_link,
        mail=mail)


@app.route("/post/<int:requested_post_id>")
def post(requested_post_id):
    # temporary way:
    for post in posts:
        if post['id'] == requested_post_id:
            found = post
            return render_template("post.html", post=found)

    
