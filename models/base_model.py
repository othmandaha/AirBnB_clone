#!/usr/bin/python3
"""Module for Base class"""
from datetime import datetime
import uuid
import models

class BaseModel:

        """Represents the BaseModel of the HBnB project."""
        def __init__(self):
                """Initialization of a Base instance."""

                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()

        def __str__(self):
                """Return the print/str representation of the BaseModel instance."""
                cla_name = self.__class__.__name__
                return "[{}] ({}) {}".format(cla_name, self.id, self.__dict__)

        def save(self):
                """Updates the updated_at attribute."""
                self.updated_at = datetime.now()

        def to_dict(self):
                """Returns a dictionary representation of an attribute."""

                the_dict = self.__dict__.copy()
                the_dict["__class__"] = self.__class__.__name__
                the_dict["created_at"] = the_dict["created_at"].isoformat()
                the_dict["updated_at"] = the_dict["updated_at"].isoformat()
                return the_dict

        


