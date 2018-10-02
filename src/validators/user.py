import re
from marshmallow import (
    Schema, fields,
    validates, ValidationError)
from src.common.mixins import BaseSchema


class UserSchema(BaseSchema):
    email = fields.String(required=True)
    password = fields.String(required=True)

    @validates('email')
    def validate_email(self, value):
        regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
        if len(value) < 3 or re.match(regex, value) is None:
            raise ValidationError('Invalid email: %s' % value)

    @validates('password')
    def validate_password(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValidationError('Email must be more than 4 characters and less than 16 characters')
