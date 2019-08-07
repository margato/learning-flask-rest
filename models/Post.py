from models import db, ma


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(8192))

    def __init__(self, title, description):
        self.title = title
        self.description = description


class PostSchema(ma.Schema):

    class Meta:
        fields = ('id', 'title', 'description')


post_schema = PostSchema(strict=True)
posts_schema = PostSchema(many=True, strict=True)
