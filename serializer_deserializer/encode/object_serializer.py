from typing import Union

from metaclass.singleton_meta import SingletonMeta

from serializer_deserializer.encode.creator import Creator as SerializerCreator
from serializer_deserializer.encode.serializers import JsonSerializer
from models.credential import ApiToken, UserPassword


serializer_creator = SerializerCreator()
serializer_creator.register(specific_type='JSON', specific_object=JsonSerializer)


class ObjectSerializer(metaclass=SingletonMeta):
    _creator = serializer_creator

    def encode_object(self, serialize_format: str, data: Union[ApiToken, UserPassword]) -> dict:
        serializer = self._creator.create(specific_type=serialize_format)
        return serializer().encode(data)
