from extensions import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id       = db.Column(db.Integer, primary_key=True)
    nombre   = db.Column(db.String(100), nullable=False)
    email    = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, nombre, email, password):
        self.nombre   = nombre
        self.email    = email
        self.password = password