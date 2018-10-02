
class BaseConfig:
    PAGE_SIZE = 10
    TOKEN_LIFE = 10 * 24 * 60 * 60 # (seconds)
    DB_URI = 'sqlite:///./recipe.db'
    SECRET_KEY = 'easy-to-guess-9876@#$!'