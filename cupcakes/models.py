from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

# Models go below
class Cupcake(db.Model):
    """Create Cupcake model to add cupcakes to database"""
    __tablename__ = "cupcakes"

    def __repr__(self):
        p = self
        return f"<Cupcake id={p.id} Cupcake_flavor={p.flavor} size={p.size}"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)

    flavor = db.Column(db.Text,
                        nullable=False)

    size = db.Column(db.Text,
                        nullable=False)

    rating = db.Column(db.Float,
                        nullable=False)

    image = db.Column(db.Text,
                        nullable=False,
                        default="https://tinyurl.com/demo-cupcake")

    def serialize(self):
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }
                        
                        
                        