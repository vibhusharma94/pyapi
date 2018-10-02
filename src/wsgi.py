import re
import traceback
import json
import types

from src.common.constants import status
from src.common.exceptions import httperrors
from src.web import Response, Request


__all__ = ('WsgiApplication',)


class WsgiApplication(object):

    routes = []
    headers = []
    db_session = None

    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response

    def __iter__(self):
        try:
            response = self.get_http_response()
        except httperrors.HttpError as err:
            response = Response(content=err.get_response(), status=err.code)
        except Exception as err:
            # raise 500 server error
            msg = traceback.format_exc().split("\n")
            response = Response(content=msg, status=status.HTTP_STATUS_500, content_type='text/plain')

        headers = response.headers + self.headers # add defaults headers
        self.start_response(response.status, headers)
        return iter([response.content])

    def get_http_response(self):
        path = self.environ.get('PATH_INFO', '')
        method = self.environ["REQUEST_METHOD"]
        callback = method.lower()
        request = Request(self.environ)

        for regex, handler in self.routes:
            match = re.match('^' + regex + '$', path)
            if match is not None:
                args = match.groups()

                # accepts plain functions
                if type(handler) is types.FunctionType:
                    return handler(request, *args)

                if not args and method == "GET" \
                            and hasattr(handler, 'list'):
                    callback = "list"
                
                try:
                    handler_callback = getattr(handler, callback)
                except AttributeError:
                    return not_allowed(method)

                handler.request = request
                handler.db_session = self.db_session
                return handler_callback(request, *args)
        return not_found(path)


def not_allowed(method):
    raise httperrors.Http405("%s not allowed"%(method))

def not_found(path):
    raise httperrors.Http404("Path %s does not exist"%(path))
