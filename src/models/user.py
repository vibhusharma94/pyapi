from passlib.hash import pbkdf2_sha256
from sqlalchemy import (Column, Integer, String)
from src.common.mixins import ObjToDictMixin
from database import Base, db_session


class User(Base, ObjToDictMixin):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)

    def __repr__(self):
        return 'id: {}, email: {}'.format(self.id, self.email)

    def password_verified(self, password):
        # verifying the password
        return pbkdf2_sha256.verify(password, self.password)

    @classmethod
    def hash_password(self, password):
        # generate new salt, and hash a password
        return pbkdf2_sha256.hash(password)


