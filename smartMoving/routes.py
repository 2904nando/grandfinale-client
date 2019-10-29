from flask import render_template, redirect, request, url_for, flash
from smartMoving.models import User, Permissao_Usuario, Permissao
from smartMoving import app

@app.route("/")
def index():
    return render_template("index.html.j2")

@app.route("/realview")
def realview():
    return render_template("realview.html.j2")

@app.route("/login")
def login():
    return render_template("login.html.j2")

@app.route("/register")
def register():
    return render_template("register.html.j2")

@app.route("/rota")
def rota():
    return render_template("rota.html.j2")

@app.route("/contato")
def contato():
    return render_template("contato.html.j2")