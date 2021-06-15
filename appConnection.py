from flask import Flask
from constants import MYSQL_CONNECTION_STRING
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = MYSQL_CONNECTION_STRING
db = SQLAlchemy(app)