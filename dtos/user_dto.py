class UserDTO:
    def __init__(self, user):
        self.id = user.id
        self.name = user.name
        self.email = user.email
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }
