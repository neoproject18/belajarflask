from app import db

class Galeri(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    filename = db.Column(db.String(50), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    pathname = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Galeri {}>'.format(self.name)