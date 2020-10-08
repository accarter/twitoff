import os
from os import getenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URL")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
# 'sqlite:///' + os.path.join(basedir, 'twitoff.db')
app.config['SQL_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'mysecretkey')

db = SQLAlchemy(app)

from twitoff.users.views import users_blueprint
from twitoff.tweets.views import tweets_blueprint

app.register_blueprint(users_blueprint, url_prefix='/user')
app.register_blueprint(tweets_blueprint, url_prefix='/tweets')
