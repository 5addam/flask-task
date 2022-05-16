# Imports
from flask import request, jsonify, Blueprint
from flask_task import db
from ..models.models import User

# init Blueprints
users = Blueprint('users', __name__)

# create db if not already created
@users.before_app_first_request
def init_db():
    db.create_all()


# @users.route('/user/new', methods=['GET'])
# def user():
#     return jsonify({'message': 'Route is working...'})

# ===================================== GET REQUESTS ROUTES =================================================
@users.route('/user/all', methods=['GET'])
def get_all_users():
    all_users_list = User.query.order_by(User.date_joined.desc())
    
    users = []
    for user in all_users_list:
        users.append(
            dict(
                id=user.id,
                name=user.name,
                email=user.email,
                password=user.password
                )
            )
    
    return jsonify({'data': users})


# ===================================== POST REQUESTS ROUTES ===========================================

@users.route('/user/new', methods=['POST'])
def new_user():
    data = request.get_json()
    print(data)
    new_user = User(name=data['name'], email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    db.session.remove()

    return jsonify({'message': 'New User Created!!'})

