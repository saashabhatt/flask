"""Models for Blogly."""
import datetime
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

# Models go below
class User(db.Model):
    __tablename__ = "users"

    def __repr__(self):
        p = self
        return f"<User id={p.id} first_name={p.first_name} last_name={p.last_name}"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    
    first_name = db.Column(db.String(50),
                            nullable=False)

    last_name = db.Column(db.String(50),
                            nullable=False)
    
    image_url = db.Column(db.String(),
                            default="http://tinyurl.com/missing-tv")



class Post(db.Model):
    __tablename__ = "posts"

    def __repr__(self):
        p = self
        return f"<User id={p.id} title={p.title}"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    
    title = db.Column(db.String(),
                            nullable=False)

    content = db.Column(db.String(),
                            nullable=False)    
    
    created_at = db.Column(db.DateTime, 
                            nullable=False,
                            default=datetime.datetime.now)
    
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'))

    userrel = db.relationship('User', backref='pst')
    

class PostTag(db.Model):
    __tablename__ = "posttags"

    post_id = db.Column(db.Integer,
                        db.ForeignKey('posts.id'),
                        primary_key=True)

    tag_id = db.Column(db.Integer,
                        db.ForeignKey('tags.id'),
                        primary_key=True)
                        
class Tag(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    
    name = db.Column(db.String(),
                    unique=True,
                    nullable=False)

    postlist = db.relationship('Post', secondary="posttags", backref='tagslist')



