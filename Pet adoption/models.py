from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

# Models go below
class Pet(db.Model):
    """Create Pet class to add pets to database"""
    __tablename__ = "pets"

    def __repr__(self):
        p = self
        return f"<Pet id={p.id} Pet_name={p.name} species={p.species}"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    
    name = db.Column(db.String(100),
                    nullable=False)

    species = db.Column(db.String(100),
                        nullable=False)
    
    photo_url = db.Column(db.String())

    age = db.Column(db.Integer)

    notes = db.Column(db.Text)

    available = db.Column(db.Boolean,
                        default=True)



