from src.common.constants import status


class HttpError(Exception):
    """Raised when HTTP error occurs"""
    code = None

    def __init__(self, msg, code=0):
        self.code = self.code if self.code else code
        self.msg = msg

    def __str__(self):
        return 'HTTP Error %s: %s' % (self.code, self.msg)

    def __repr__(self):
        return '<HTTPError %s: %r>' % (self.code, self.msg)

    def get_response(self):
        return { 
            "msg": self.msg,
            "status_code": self.code,
            "status": status.STATUS_MAP[self.code],
        }


class Http400(HttpError):
    code = 400

class Http401(HttpError):
    code = 401

class Http403(HttpError):
    code = 403

class Http404(HttpError):
    code = 404

class Http405(HttpError):
    code = 405

class Http500(HttpError):
    code = 500
