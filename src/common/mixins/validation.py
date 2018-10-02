from marshmallow import Schema, ValidationError


class BaseSchema(Schema):

    def is_valid(self, data):
        try:
            self.data = self.load(data)
            return True
        except ValidationError as err:
            self.errors = err.messages
            return False