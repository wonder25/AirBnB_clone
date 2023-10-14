#!/usr/bin/python3
"""
BaseModel Module
"""

import datetime
import uuid


class BaseModel:
    """
    Class Docs
    Defines all common attributes
    """
    def __init__(self, *args, **kwargs):

        """
        Docs
        Object initialiser
        """
        from models import storage
        if kwargs:
            for a, b in kwargs.items():
                if a in ("created_at", "updated_at"):
                    self.__dict__[a] = datetime.datetime.\
                            strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                elif a == "__class__":
                    continue
                else:
                    self.__dict__[a] = b

        self.id = str = str(uuid.uuid4())
        self.created_at = darerime.datetime.now()
        self.updated_at = datetime.datetime.now()
        storage.new(self)

    def __str__(self):

        """
        Docs
        Prints the string rep of the object
        """

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Docs
        updates when the object is modified
        """

        from models import storage
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """
        Docs
        Returns a dictionary rep of the object
        """

        dict = {}
        dict["__class__"] = self.__class__.__name__

        for a, b in self.__dict__.items():
            if isinstance(b, datetime.datetime):
                b = b.isoformat()
                dict[a] = b
            dict[a] = b

        return dict
