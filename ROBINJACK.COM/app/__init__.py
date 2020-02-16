from flask import Flask
import configparser
from flask_wtf.csrf import CSRFProtect
import os

from flask_migrate import Migrate

dir_path = '/Users/robinjack/Documents/Birkbeck_masters/Project/bbk/ROBINJACK.COM'


config = configparser.ConfigParser()

if os.environ.get("HOME") =='/app':
    f = '/app/config.cfg'

else:
    working_directory = os.environ.get('WD', dir_path)
    f = working_directory + '/app/config.cfg'

config.read(f)

app = Flask(__name__)
app.config.from_object(config)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['DATABASE_URL'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ['SQLALCHEMY_TRACK_MODIFICATIONS']


from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)


from app import routes, models

