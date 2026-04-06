from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from flask import Flask, flash, request, redirect


app = Flask(__name__)


UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER


app.config['SECRET_KEY'] = '8ea2a86e42689205dde0ba81f31138b6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chatbot.db'

db = SQLAlchemy(app)

login_manager = LoginManager(app) 


from chatbot import routes
app.app_context().push()