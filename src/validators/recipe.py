from marshmallow import (
    Schema, fields,
    validates, ValidationError)
from src.common.mixins import BaseSchema


class RecipeSchema(BaseSchema):
    name = fields.String(required=True)
    preptime = fields.Integer(required=True)
    difficulty = fields.Integer(required=True)
    vegetarian = fields.Boolean(required=True)

    @validates('name')
    def validate_name(self, value):
        if len(value) == 0:
            raise ValidationError('Value is required')

    @validates('difficulty')
    def validate_difficulty(self, value):
        if value not in range(1, 4):
            raise ValidationError('Invalid value. accepted values are (1-3)')

    @validates('preptime')
    def validate_preptime(self, value):
        if value < 1:
            raise ValidationError('Value can not be less than 1')


class RatingSchema(BaseSchema):
    value = fields.Integer(required=True)
    
    @validates('value')
    def validate_value(self, value):
        print(value)
        if value not in range(1, 6):
            raise ValidationError('Invalid value. accepted values are (1-5)')

