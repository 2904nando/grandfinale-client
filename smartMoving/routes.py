from flask import render_template, redirect, request, url_for, flash
from smartMoving import app
from smartMoving.forms import FormularioRegistro, FormularioLogin

@app.route("/")
def index():
    return render_template("index.html.j2")

@app.route("/realview")
def realview():
    return render_template("realview.html.j2")

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = FormularioLogin()
    if form.validate_on_submit():
        if form.email.data == 'nando@kyan.com.br' and form.password.data == 'password':
            flash(f'Logado com sucesso!', 'success')
            return redirect(url_for("index"))
        else:
            flash(f'Credenciais inválidas!', 'danger')
    return render_template("login.html.j2", form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = FormularioRegistro()
    if form.validate_on_submit():
        flash(f'Conta criada com sucesso! Usuário: {form.username.data}.', 'success')
        return redirect(url_for("index"))
    else:
        print(form.errors)
    return render_template("register.html.j2", form=form)

@app.route("/rota")
def rota():
    return render_template("rota.html.j2")

@app.route("/contato")
def contato():
    return render_template("contato.html.j2")