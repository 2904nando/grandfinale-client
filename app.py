from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html.j2")

@app.route("/realview")
def realview():
    return render_template("realview.html.j2")

@app.route("/login")
def login():
    return render_template("login.html.j2")

@app.route("/rota")
def rota():
    return render_template("rota.html.j2")

@app.route("/contato")
def contato():
    return render_template("contato.html.j2")

if __name__ == "__main__":
    app.run(debug=True)