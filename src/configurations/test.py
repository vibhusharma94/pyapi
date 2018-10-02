from .common import BaseConfig


class TestConfig(BaseConfig):
    DB_URI = 'sqlite:///./recipe_test.db'