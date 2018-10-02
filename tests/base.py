import unittest
from werkzeug.test import Client
from werkzeug.wrappers import BaseResponse

from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine

from src.app import application
from src.configurations import TestConfig
from src.models import Recipe
from src.utils import encode_auth_token
from database import Base


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        super(BaseTestCase, self).setUp()
        self.test_client = Client(application, BaseResponse)
        self.engine = create_engine(TestConfig.DB_URI)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(autocommit=False,
                       autoflush=False,
                       bind=self.engine)
        self.session = scoped_session(Session)
        data = {
            "name":"Coffee",
            "difficulty": 1,
            "preptime": 5,
            "vegetarian": True
        }
        instance = Recipe(**data)
        self.session.add(instance)
        self.session.commit()
        self.recipe = instance
        print(instance.id)
        self.headers = {'Content-Type': 'application/json',
                   'ACCESS-TOKEN': encode_auth_token(4563754)}

    def tearDown(self):
        Base.metadata.drop_all(self.engine)
        self.session.close()
        super(BaseTestCase, self).tearDown()
