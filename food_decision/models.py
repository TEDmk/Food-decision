from sqlalchemy.orm import mapped_column
from food_decision import db


class User(db.Model):
    __tablename__ = 'user'
    id = mapped_column(db.Integer, primary_key=True)
    name = mapped_column(db.String(50), unique=False)
    email = mapped_column(db.String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return f'<User {self.name!r}>'
