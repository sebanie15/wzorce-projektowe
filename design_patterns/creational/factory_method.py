from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def do_stuff(self):
        pass


class ConcreteProductA(Product):
    def do_stuff(self):
        print(f'Me ConcreteProductA class doing stuff!')


class ConcreteProductB(Product):
    def do_stuff(self):
        print(f'Me ConcreteProductB class doing stuff!')


class Creator(ABC):

    def some_operation(self):
        product = self.create_product()
        product.do_stuff()
        return product

    @abstractmethod
    def create_product(self) -> Product:
        pass


class ConcreteCreatorA(Creator):

    def create_product(self):
        return ConcreteProductA()


class ConcreteCreatorB(Creator):

    def create_product(self):
        return ConcreteProductB()


if __name__ == '__main__':

    a = ConcreteProductB()
    # ...
    a.do_stuff()

    concrete_creator_a = ConcreteCreatorA()
    truck = concrete_creator_a.some_operation()

    concrete_creator_b = ConcreteCreatorB()
    ship = concrete_creator_b.some_operation()
