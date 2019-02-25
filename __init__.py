from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config


app = Flask(__name__, instance_relative_config=True)
db = SQLAlchemy(app)
app.config.from_object(app_config['development'])
# app.config.from_pyfile('config.py')
import views
import models
