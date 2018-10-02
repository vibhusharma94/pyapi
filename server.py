import os
import sys

if __name__ == "__main__":
    os.environ['deploy'] = 'dev'
    from wsgiref.simple_server import make_server
    from src.app import application
    try:
        print("Serving on 0.0.0.0:8000 ...")
        make_server('0.0.0.0', 8000, application).serve_forever()
    except KeyboardInterrupt:
        pass
