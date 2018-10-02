import datetime
import jwt

from sqlalchemy.orm.util import class_mapper
from src.common.exceptions import httperrors
from src.configurations import CONFIG


def get_object_or_404(db_session, model, pk=None):
    try:
        class_mapper(model)
    except:
        raise ValueError(
            "First argument to get_object_or_404() must be a Model")
    try:
        pk = int(pk)
    except (ValueError, TypeError):
        raise httperrors.Http404("object not found")
    obj = db_session.query(model).get(pk)
    if not obj:
        raise httperrors.Http404("object not found")
    return obj


def decode_auth_token(auth_token):
    try:
        payload = jwt.decode(auth_token, CONFIG.SECRET_KEY)
        return payload['sub']
    except jwt.ExpiredSignatureError:
        msg = 'Signature expired.'
        raise httperrors.Http401(msg)
    except jwt.InvalidTokenError:
        msg = 'Invalid token.'
        raise httperrors.Http401(msg)


def encode_auth_token(user_id):
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=CONFIG.TOKEN_LIFE),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(payload, CONFIG.SECRET_KEY, algorithm='HS256')
    except Exception as e:
        return e


def auth_enabled(f):
    def wrap(view, *args, **kwargs):
        from src.models import User
        auth_token = view.request.headers.get("Access-Token")
        if not auth_token:
            raise httperrors.Http401("No authorization token provided")
        user_id = decode_auth_token(auth_token)
        user = view.db_session.query(User).get(user_id)
        if not user:
            raise httperrors.Http401("Invalid token")
        return f(view, *args, **kwargs)
    return wrap
