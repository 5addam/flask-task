from flask import jsonify, Blueprint
from flask_task import db

main = Blueprint('main', __name__)


@main.route("/")
def home():
    return jsonify({'message': 'Hello Flask User!!'})
