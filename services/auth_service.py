from models.usuario import Usuario
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
import jwt, datetime
from config import Config

class AuthService:

    def register(self, nombre, email, password):
        hashed = generate_password_hash(password)
        usuario = Usuario(nombre=nombre, email=email, password=hashed)
        db.session.add(usuario)
        db.session.commit()
        return usuario

    def login(self, email, password):
        usuario = Usuario.query.filter_by(email=email).first()

        if not usuario or not check_password_hash(usuario.password, password):
            return None

        token = jwt.encode({
            "user_id": usuario.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
        }, Config.SECRET_KEY, algorithm="HS256")

        return token
