from core.extensions import db

class Item(db.Model):
    print("tess")
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<Item {self.name}>'
