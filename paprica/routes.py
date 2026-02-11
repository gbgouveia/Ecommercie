from paprica import app
from flask import render_template
from paprica.models import Item

@app.route('/')
def page_home():
    return render_template("home.html")

@app.route('/produtos')
def page_produto():
    itens=Item.query.all()

    return render_template("produtos.html",itens=itens) 

@app.route('/')
def page_login():
    return render_template("login.html")

@app.route('/')
def page_cadastro():
    return render_template("cadastro.html")