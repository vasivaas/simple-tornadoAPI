from collections import defaultdict


class SingletonMeta(type):
    _singleton_instances = defaultdict(int)

    def __call__(cls, *args, **kwargs):
        if cls not in cls._singleton_instances:
            new_instance = super().__call__(*args, **kwargs)
            cls._singleton_instances[cls] = new_instance
        return cls._singleton_instances[cls]
