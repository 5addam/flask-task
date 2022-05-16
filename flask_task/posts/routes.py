# Imports
from flask import request, jsonify, Blueprint
from flask_task import db
from ..models.models import Post

# init Blueprints
posts = Blueprint('posts', __name__)

# create db if not already created
@posts.before_app_first_request
def init_db():
    db.create_all()


# ===================================== GET REQUESTS ROUTES =================================================
@posts.route('/post/all', methods=['GET'])
def get_all_posts():
    posts_list = Post.query.order_by(Post.date_posted.desc())
    
    posts = []
    for post in posts_list:
        posts.append(
            dict(
                id=post.id,
                title=post.title,
                content=post.content,
                date_posted=post.date_posted
                )
            )
    
    return jsonify({'data': posts})


# ===================================== POST REQUESTS ROUTES ===========================================

@posts.route('/post/new', methods=['POST'])
def new_post():
    data = request.get_json()
    new_post = Post(title=data['title'], content=data['content'])
    db.session.add(new_post)
    db.session.commit()
    db.session.remove()

    return jsonify({'message': 'New Post Created!!'})

