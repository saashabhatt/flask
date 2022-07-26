
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

bcrypt = Bcrypt()

def connect_db(app):
    db.app = app
    db.init_app(app)

# Models go below
class User(db.Model):
    """Create Users model to add users to database"""
    __tablename__ = "users"

    def __repr__(self):
        p = self
        return f"<User username={p.username} User_firstname={p.first_name} User_lastname={p.last_name}"

    username = db.Column(db.String(20),
                    primary_key=True,
                    unique=True,
                    nullable=False)

    password = db.Column(db.Text,
                        nullable=False)

    email = db.Column(db.String(50),
                        unique=True,
                        nullable=False)

    first_name = db.Column(db.String(30),
                        nullable=False)

    last_name = db.Column(db.String(30),
                        nullable=False)

    @classmethod
    def register(cls, username, pwd, email, first_name, last_name):
        hashed = bcrypt.generate_password_hash(pwd)
        hashed_utf8 = hashed.decode("utf8")

        return cls(username=username, 
                password=hashed_utf8,
                email = email,
                first_name=first_name,
                last_name=last_name)
    
    @classmethod
    def authenticate(cls, username, pwd):
        u = User.query.filter_by(username=username).first()

        if u and bcrypt.check_password_hash(u.password, pwd):
            return u 
        else:
            return False

class Feedback(db.Model):
    """Create Users model to add users to database"""
    __tablename__ = "feedbacks"

    def __repr__(self):
        p = self
        return f"<Feedback username={p.username} User_title={p.title}"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)

    title = db.Column(db.String(100),
                        nullable=False)

    content = db.Column(db.Text,
                        nullable=False)

    username = db.Column(db.String(20),
                        db.ForeignKey('users.username'))

    user = db.relationship('User', backref="feedback")