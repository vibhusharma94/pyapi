import enum
from datetime import datetime

from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy_utils.types.choice import Choice


__all__ = ('ObjToDictMixin',)


class ObjToDictMixin(object):
    """
    Comvert sqlalchemy object to dict.
    """

    def __iter__(self):
        return self.to_dict().iteritems()

    def to_dict(self, skip_fields=[]):
        res = {column.key: getattr(self, attr)
               for attr, column in self.__mapper__.c.items()}
        for field in skip_fields:
            res.pop(field, '')
        for key, value in res.items():
            if isinstance(value, datetime):
                res[key] = value.isoformat()
            if isinstance(value, Choice):
                res[key] =  str(value.value)
            if isinstance(value, enum.Enum):
                res[key] = value.value

        return res
