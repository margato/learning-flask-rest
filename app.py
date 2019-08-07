from flask import Flask
from models import db, ma
from routes.posts import posts_route_blueprint
import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Init Flask
app = Flask(__name__)

# Register routes
app.register_blueprint(posts_route_blueprint)

# Set SQLAlchemy config
app.config['SECRET_KEY'] = 'this_is_secret_af'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'crud_example.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init SQLAlchemy and Marshmallow
db.init_app(app)
ma.init_app(app)
with app.app_context():
    db.create_all()

# Run server
if __name__ == "__main__":
    app.run(debug=True)
