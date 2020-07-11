from app import app
from flask import render_template, request


@app.errorhandler(404)
def not_found(e):
    error_code = 404
    header = "Nie znaleziono!"
    message = "Nie ma tu nic ciekawego."
    return render_template("error.html",
                        error_code = error_code,
                        header = header,
                        message = message)


@app.errorhandler(500)
def internal(e):
    error_code = 500
    header = "Ups, mamy problem!"
    message = "Blad wystapil po stronie serwera."
    return render_template("error.html",
                        error_code = error_code,
                        header = header,
                        message = message)