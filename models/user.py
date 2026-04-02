from extensions import db

class User(db.Model):
    __tablename__ = 'UsersSecurity'
    
    id       = db.Column(db.Integer, primary_key=True)
    name   = db.Column(db.String(100), nullable=False)
    email    = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, name, email, password):
        self.name   = name
        self.email    = email
        self.password = password