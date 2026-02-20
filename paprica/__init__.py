from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///paprica.db"
app.config["SECRET_KEY"] = '8697d8a1ec77e8c9b434ae5a'
db.init_app(app)

from paprica import routes