"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns dictionary representation of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        c_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(c_name, obj.id)] = obj

    def save(self):
        """serialize __objects to __file_path."""
        the_dict = FileStorage.__objects
        form_dict = {obj: the_dict[obj].to_dict() for obj in the_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(form_dict, f)

    def reload(self):
        """deserialize __file_path to __obejcts if it exists."""
        try:
            with open(FileStorage.__file_path, "r") as f:
                objects_dict = json.load(f)
                for o in objects_dict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
