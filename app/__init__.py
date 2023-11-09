from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DB_PASSWORD


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{DB_PASSWORD}@localhost/app'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes, models
