import uuid, json
from dataclasses import dataclass
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.postgresql import UUID

from food_decision import db


class Recipe(db.Model):
    __tablename__ = 'recipe'
    id = mapped_column(db.String(50), primary_key=True, default=str(uuid.uuid4()))
    name = mapped_column(db.String(50), unique=False, nullable=False)
    description = mapped_column(db.Text, unique=False, nullable=False)
    persons = mapped_column(db.Integer, nullable=False)
    ingredients = mapped_column(db.JSON, nullable=False)
    tags = mapped_column(db.JSON, nullable=False)

    # def __repr__(self):
    #     return f'<Meal {self.name!r}>'


@dataclass
class DataRecipe:   # Add validation functions
    name: str
    description: str
    persons: int
    ingredients: json
    tags: json
