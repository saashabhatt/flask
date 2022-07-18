"""Models for Blogly."""
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

    @classmethod
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"