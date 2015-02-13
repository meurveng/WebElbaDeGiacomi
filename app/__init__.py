#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import *
from Connection import *
from Clases import *

app = Flask(__name__)
app.secret_key = "clave"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/mongo")
def mongo():
	user = Usuario("meurveng", "contrasena")
	connection(user.usuario, user.contrasena)
	return render_template("correcto.html")

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    flash("Te has desconectado")
    return redirect(url_for("login"))

@app.route("/correcto")
def correcto():
    return render_template("correcto.html")

@app.route("/login", methods = ["GET", "POST"])
def log():
	error = None
	if request.method == "POST":
		if request.form["username"] != "admin" or request.form["password"] != "admin":
			error = "Credenciales no validas"
		else:
			session["logged_in"] = True
			return redirect(url_for("correcto"))
	else:
		error = "Metodo no aceptado"
	return render_template("login.html", error=error)

if __name__ == "__main__":
    app.run()