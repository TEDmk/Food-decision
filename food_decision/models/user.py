from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import mapped_column

from food_decision.db import Base


class User(Base):
    __tablename__ = 'users'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(50), unique=True)
    email = mapped_column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return f'<User {self.name!r}>'

