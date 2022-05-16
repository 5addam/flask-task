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
app.config['SQLALCHEMY_POOL_SIZE'] = 100
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0
app.config['SQLALCHEMY_POOL_RECYCLE'] = 50
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 300
# Init Db
db = SQLAlchemy(app, session_options={'autocommit': True})


# Blueprints
from .main.routes import main
from .users.routes import users
from .posts.routes import posts

app.register_blueprint(main)
app.register_blueprint(users)
app.register_blueprint(posts)
