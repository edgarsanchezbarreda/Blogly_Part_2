"""Models for Blogly."""

from http import server
from turtle import title
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()

default_image_url = 'https://merriam-webster.com/assets/mw/images/article/art-wap-article-main/egg-3442-e1f6463624338504cd021bf23aef8441@1x.jpg'

def connect_db(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column (
        db.Integer,
        primary_key = True,
        autoincrement = True
    )

    first_name = db.Column (
        db.Text,
        nullable = False
    )

    last_name = db.Column (
        db.Text,
        nullable = False
    )

    image_url = db.Column (
        db.Text,
        nullable = True,
        default = default_image_url
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(
        db.Integer,
        primary_key = True,
        autoincrement = True
    )

    title = db.Column(
        db.Text,
        nullable = False
    )

    content = db.Column(
        db.String(50),
        nullable = False
    )

    created_at = db.Column(
        db.DateTime,
        nullable = False,
        server_default = func.now()
    )

    user_id = db.Column(
        db.Text,
        db.ForeignKey('user.id')
    )