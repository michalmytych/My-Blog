# -*- coding: utf-8 -*-
from flask import render_template
from app import app


@app.route("/admin")
def admin():
    title = "Index of Admin"
    return render_template("admin/index.html", title=title)


@app.route("/admin/dashboard")
def admin_dashboard():
    title = "Dashboard"
    return render_template("admin/index.html", title=title)



@app.route("/admin/posts")
def admin_posts():
    title = "Posts"
    return render_template("admin/index.html", title=title)

