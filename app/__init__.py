from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://ztvbiiivxsawfs:16de43389c49fa6c20f0ddd56cd6d5036a6ec0cd09e6d9bed69eceba23d2c643@ec2-107-20-177-161.compute-1.amazonaws.com:5432/d71i118gk8v99j"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning


# UPLOAD_FOLDER = './app/static/images' 
app.config['UPLOAD_FOLDER'] = './app/static/images'

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views