class ApiToken:
    def __init__(self, params: dict) -> None:
        self.token = params.get('token', None)

    def encode(self, serializer) -> None:
        serializer.initial_dict()
        serializer.add_property(property_name='token', property_value=self.token)

    def is_valid(self) -> bool:
        return self.token is not None


class UserPassword:
    def __init__(self, params: dict) -> None:
        self.user = params.get('user', None)
        self.password = params.get('password', None)

    def encode(self, serializer) -> None:
        serializer.initial_dict()
        serializer.add_property(property_name='user', property_value=self.user)
        serializer.add_property(property_name='password', property_value=self.password)

    def is_valid(self) -> bool:
        return (self.user and self.password) is not None
