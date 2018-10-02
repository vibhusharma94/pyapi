import os
from .common import BaseConfig


class ProdConfig(BaseConfig):
    DATABASE = {
        'user': os.environ.get('POSTGRES_USER', 'hellofresh'),
        'pw': os.environ.get('POSTGRES_PASSWORD', 'hellofresh'),
        'db': os.environ.get('POSTGRES_DB', 'hellofresh'),
        'host': os.environ.get('POSTGRES_HOST', 'db'),
        'port': '5432',
    }
    DB_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % DATABASE