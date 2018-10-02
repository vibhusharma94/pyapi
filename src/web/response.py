import json
from src.common.constants import status

__all__ = ('Response',)


class Response(object):
    """
    A wraper for http response. 
    """

    def __init__(self, content=b'', status=200, content_type='application/json'):
        self.content_type = content_type
        self.header_dict = { 
            "Content-Type": content_type
        }
        self._headers = []
        self.status_code = status
        self.content = content

    def set_header(self, key, value):
        self.header_dict[key] = value

    @property
    def headers(self):
        self._headers = []
        for k,v in self.header_dict.items():
            self._headers.append((k, v))
        return self._headers

    @property
    def status(self):
        if self.status_code in status.STATUS_MAP:
            return status.STATUS_MAP[self.status_code]
        print("Warning! Status %s does not exist!"%(self.status_code))
        return status.STATUS_MAP[577]

    @property
    def content(self):
        return b''.join(self._container)

    @content.setter
    def content(self, value):
        value = json.dumps(value, cls=BytesEncoder)
        
        if isinstance(value, bytes):
            content =  bytes(value)
        elif isinstance(value, str):
            content =  bytes(value.encode('utf-8'))
        else:
            content =  str(value).encode('utf-8')

        self._container = [content]


class BytesEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return obj.decode('utf-8')
        return json.JSONEncoder.default(self, obj)

