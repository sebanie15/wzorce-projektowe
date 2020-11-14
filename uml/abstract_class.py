from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def get_brand(self):
        pass


class Mercedes(Car):
    def get_brand(self):
        return "Mercedes"


class Toyota(Car):
    def get_brand(self):
        return "Toyota"
