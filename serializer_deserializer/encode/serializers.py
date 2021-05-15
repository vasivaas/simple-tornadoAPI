from typing import Union
from bson import ObjectId

from metaclass.singleton_meta import SingletonMeta
from models.credential import ApiToken, UserPassword


class JsonSerializer(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self._current_object = None

    def initial_dict(self) -> None:
        self._current_object = {'_id': str(ObjectId())}

    def add_property(self, property_name: str, property_value: str) -> None:
        self._current_object[property_name] = property_value

    def encode(self, object_to_encode: Union[ApiToken, UserPassword]) -> dict:
        if hasattr(object_to_encode, 'encode'):
            object_to_encode.encode(self)
            return self._current_object
