from __future__ import annotations


class Singleton:
    _INSTANCE = None

    MAX_USER_AMOUNT = 100

    def __init__(self):
        raise NotImplementedError('Creation of singleton instance with constructor is forbidden')

    @classmethod
    def get_instance(cls) -> Singleton:
        if not cls._INSTANCE:
            cls._INSTANCE = cls.__new__(cls)
        return cls._INSTANCE


if __name__ == '__main__':
    instance_1 = Singleton.get_instance()
    instance_2 = Singleton.get_instance()
    print(instance_1)
    print(instance_1 == instance_2)
    assert instance_1 is instance_2
