# Imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Init app
app = Flask(__name__)
app.config["SECRET_KEY"] = 'b6b4735224de8d561a0878b88a498729'
basedir = os.path.abspath(os.path.dirname(__file__))

# setup Db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/mysite'
# Init Db
db = SQLAlchemy(app)


# Blueprints
from .main.routes import main
from .users.routes import users
from .posts.routes import posts

app.register_blueprint(main)
app.register_blueprint(users)
app.register_blueprint(posts)
