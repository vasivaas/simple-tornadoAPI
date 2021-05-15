class Creator:
    def __init__(self) -> None:
        self._objects = {}

    def register(self, specific_type: str, specific_object) -> None:
        self._objects[specific_type] = specific_object

    def create(self, specific_type: str):
        current_object = self._objects.get(specific_type)
        if current_object is None:
            raise ValueError(specific_type)
        else:
            return current_object
