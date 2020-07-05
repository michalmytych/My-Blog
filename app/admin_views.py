# -*- coding: utf-8 -*-

from app import app


@app.route("/admin/dashboard")
def admin_dashboard():
    return "here will be admin's dashboard"


@app.route("/admin/posts")
def admin_posts():
    return "here will be admin's posts section"

