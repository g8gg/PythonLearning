from flask import Flask
from config import DevConfig
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)


@app.route('/')
def home():
    return '<h1>你好,Flask!</h1>'


if __name__ == '__main__':
    app.run()


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    # posts = db.relationship(
    #     'Post',
    #     backref=db.backref('post', lazy='subquery')
    # )
    posts = db.relationship(
            'Post',
            backref='post',
            lazy='subquery'
    )

    # 坑爹的<<Mastering Flask>>demo, bug fixed.

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return "<User '{}'>".format(self.username)


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime())
    posts = db.relationship(
            'Comment',
            backref='post',
            lazy='dynamic'
    )
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return "<Post '{}'>".format(self.title)


class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text())
    date = db.Column(db.DateTime())
    post_id = db.Column(db.Integer(), db.ForeignKey('post.id'))

    def __repr__(self):
        return "<Comment '{}'>".format(self.text[:15])
