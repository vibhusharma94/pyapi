from src.common.mixins import HttpHandler
from src.web.response import Response
from src.validators import UserSchema
from src.common.constants import status
from src.models import User
from src.utils import encode_auth_token



class UserHandler(HttpHandler):
    """
        Create User account. 
    """
    methods = ['post']

    def post(self, request):
        schema = UserSchema()
        if schema.is_valid(request.data):

            email = schema.data['email'].lower()
            password = schema.data['password']
            user = self.db_session.query(User).filter_by(email=email).first()

            if not user:
                salted_hash = User.hash_password(password)
                user = User(email=email, password=salted_hash)
                self.db_session.add(user)
                self.db_session.commit()
                return Response(content=user.to_dict(skip_fields=['password']),
                                status=status.HTTP_STATUS_201)

            msg = {'msg': 'User already exist with email: %s' % email}
            return Response(content=msg, status=status.HTTP_STATUS_400)

        return Response(content=schema.errors, status=status.HTTP_STATUS_400)


class UserAuthHandler(HttpHandler):
    """
        Login user with email and pass and Returns JWT access token.
    """
    methods = ['post']

    def post(self, request):
        schema = UserSchema()
        if schema.is_valid(request.data):

            email = schema.data['email'].lower()
            password = schema.data['password']
            user = self.db_session.query(User).filter_by(email=email).first()

            if user and user.password_verified(password):
                data = {'Access-Token': encode_auth_token(user.id)}
                return Response(content=data, status=status.HTTP_STATUS_200)

            msg = {'msg': 'Invalid email or password'}
            return Response(content=msg, status=status.HTTP_STATUS_400)

        return Response(content=schema.errors, status=status.HTTP_STATUS_400)
