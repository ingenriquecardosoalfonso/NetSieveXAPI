class UsuarioDTO:
    def __init__(self, usuario):
        self.id = usuario.id
        self.nombre = usuario.nombre
        self.email = usuario.email

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email
        }
