import json
from cgi import parse_qsl
from src.common.exceptions import httperrors


__all__ = ('Request',)


class Request(object):
    """ 
    Request object which get passed to http handler callback as a argument.
    """

    def __init__(self,  environ):
        self._headers = None
        self._args = None
        self._body = None
        self._data = None

        self.path = environ.get('PATH_INFO', '')
        self.method = environ["REQUEST_METHOD"].lower()
        self.environ = environ
    
    def get_header(self, name, default=None):
        return self.headers.get(name.title(), default)

    @property
    def headers(self):
        if self._headers is not None:
            return self._headers
        self._headers = {}
        for key, value in self.environ.items():
            if key == "CONTENT_TYPE" or key == "CONTENT_LENGTH":
                header = key.title().replace("_", "-")
                self._headers[header] = value
            elif key.startswith("HTTP_"):
                header = key[5:].title().replace("_", "-")
                self._headers[header] = value
        return self._headers

    @property
    def args(self):
        if self._args is not None:
            return self._args
        qs = self.environ["QUERY_STRING"]
        pairs = parse_qsl(qs)
        self._args = dict(pairs) if pairs else {}
        return self._args
 
    @property
    def body(self):
        """
        parse http body
        """
        if self._body is not None:
            return self._body
        try:
            length = int(self.environ.get("CONTENT_LENGTH", "0"))
        except ValueError:
            length = 0
        if length > 0:
            self._body = self.environ['wsgi.input'].read(length)
        else:
            self._body = ''

        return self._body

    @property
    def data(self):
        if self._data is not None:
            return self._data
        if self.body:
            try:
                self._data = json.loads(self.body.decode('utf-8'))
            except Exception:
                raise httperrors.Http400("Expected JSON in request body")
        else:
            self._data = {}

        return self._data

