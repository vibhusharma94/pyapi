

class HttpHandler(object):
    """ 
	Base handler class. All Http handlers should implements this class.
	"""

    request = None 
    db_session = None
    methods = None
    HTTP_METHODS = ['GET', 'POST', 'PUT', 'DELETE']

    def __init__(self):
        if not isinstance(self.methods, list):
            raise ValueError('methods must be type of list')
        for method in self.methods:
            if not isinstance(method, str):
                raise ValueError('Invalid Http method: %s' %method)
            if method.upper() not in self.HTTP_METHODS:
                raise ValueError('Invalid Http method: %s' %method)
