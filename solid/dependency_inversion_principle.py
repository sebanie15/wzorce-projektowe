from abc import ABC, abstractmethod


class Product(ABC):

    @abstractmethod
    def get_reviews(self):
        pass


class Computer(Product):
    def get_reviews(self):
        pass

    def get_specs(self):
        pass


class Software(Product):
    def get_reviews(self):
        pass

    def get_requirements(self):
        pass


class Favourites:
    def __init__(self):
        self._favourites = []

    def add_product(self, product: Product):
        self._favourites.append(product)

    # def add_computer(self, computer: Computer):
    #     self._favourites.append(computer)
    #
    # def add_software(self, software: Software):
    #     self._favourites.append(software)
