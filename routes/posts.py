from flask import Blueprint, request, jsonify
from models.Post import Post, post_schema, posts_schema
from models import db
posts_route_blueprint = Blueprint('routes', __name__)


@posts_route_blueprint.route("/posts/create", methods=['POST'])
def create_post():
    # Define post data
    data = request.json
    title = data['title']
    description = data['description']

    # New post
    new_post = Post(title=title, description=description)
    db.session.add(new_post)
    db.session.commit()
    return jsonify(status="Post created", post=post_schema.dump(new_post))


@posts_route_blueprint.route("/posts/update/<id>", methods=['PUT'])
def update_post(id):
    post = Post.query.get(id)

    # Define put data
    data = request.json
    title = data['title']
    description = data['description']

    post.title = title
    post.description = description

    db.session.commit()
    return jsonify(status="Post updated", post=post_schema.dump(post))


@posts_route_blueprint.route("/posts/view", methods=['GET'])
def get_posts():
    all_posts = Post.query.all()
    result = posts_schema.dump(all_posts)
    return jsonify(result)


@posts_route_blueprint.route("/posts/view/<id>", methods=['GET'])
def get_single_post(id):
    post = Post.query.get(id)
    return jsonify(post)


@posts_route_blueprint.route("/posts/delete/<id>", methods=['DELETE'])
def delete_post(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return jsonify(status="Post deleted", post=post_schema.dump(post))
