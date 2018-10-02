import enum
from decimal import Decimal
from sqlalchemy import (Column, Integer, String, Boolean, ForeignKey)
from sqlalchemy_utils.types.choice import ChoiceType
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from src.common.mixins import ObjToDictMixin
from database import Base, db_session



class RatingChoice(enum.Enum):
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5


class Recipe(Base, ObjToDictMixin):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    preptime = Column(Integer, nullable=False)
    difficulty = Column(Integer, nullable=False)
    vegetarian = Column(Boolean, nullable=False)

    ratings = relationship('RecipeRating', cascade="all, delete-orphan")

    def __repr__(self):
        return 'id: {}, name: {}'.format(self.id, self.name)

    @property
    def avg_rating(self):
        value = db_session.query(func.avg(RecipeRating.value).label('average'))\
                .filter(RecipeRating.recipe_id==self.id).scalar()
        if value:
            value = Decimal(value)
            value = float(round(value, 1))
        return value

class RecipeRating(Base, ObjToDictMixin):
    __tablename__ = 'recipe_rating'

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey(Recipe.id, ondelete='CASCADE'))
    value = Column(ChoiceType(RatingChoice, impl=Integer()))
    value2 = Column(ChoiceType(RatingChoice, impl=Integer()))
    ratings = relationship("Recipe")

    def __repr__(self):
        return 'id: {}, rating: {}'.format(self.id, self.value)



