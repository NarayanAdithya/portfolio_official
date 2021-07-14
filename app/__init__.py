from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy


#App Declarations
application=Flask(__name__)
application.config.from_object(config)

from app import routes, models