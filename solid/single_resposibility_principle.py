from typing import List


class Computer:

    def __init__(self):
        self._brand = None
        self._model = None

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value


class Inventory:

    def __init__(self):
        self.computers = List[Computer]

    def search_inventory(self, computer: Computer):
        pass
