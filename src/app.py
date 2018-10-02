from src.wsgi import WsgiApplication
from src.routers import ROUTES
from database import db_session


class application(WsgiApplication):
    routes = ROUTES
    headers = [("Content-Type", "application/json")]
    db_session = db_session
