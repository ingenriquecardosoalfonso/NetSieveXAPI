from models.user import User
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
import jwt, datetime
from config import Config

class AuthService:

    def register(self, name, email, password):
        hashed = generate_password_hash(password)
        user = User(name=name, email=email, password=hashed)
        db.session.add(user)
        db.session.commit()
        return user

    def login(self, email, password):
        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            return None

        token = jwt.encode({
            "user_id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
        }, Config.SECRET_KEY, algorithm="HS256")

        return token
