# -*- coding: utf-8 -*-
from flask import render_template, url_for
from app import app


@app.route("/admin")
def admin():
    title = "Index of Admin"
    return render_template('admin.html',title=title)


@app.route("/admin/dashboard")
def admin_dashboard():
    title = "Dashboard"
    return render_template('admin.html',title=title)


@app.route("/admin/posts")
def admin_posts():
    title = "Posts"
    return render_template('posts.html',title=title)


@app.route("/admin/posts/new")
def admin_new_post():
    title = "New post"
    return render_template('newpost.html',title=title)
