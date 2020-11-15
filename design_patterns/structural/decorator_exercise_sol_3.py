"""
PIZZERIA

Korzystając z wzorca projektowego Decorator stworzmy system pozwalający złożyć pizze o dowolnych kombinacjach
składników.
Do tego celu posłuż się podstawową strukturą dekoratora.
Chcemy aby podstawową klasą była klasa PlainPizza. Pizza posiada już swoją cenę. Każdy następny składnik powinien
zwiększać cenę pizzy.
*   Gotowa pizza za pomocą metody get_cost() zwraca docelowy koszt pizzy.
*   Gotowa pizza za pomocą metody get_description() zwraca string zawierający wszystkie składniki pizzy.

Przykładowo mamy do dyspozycji następujące składniki: Mozzarella, Ham, Mushrooms, Salami. KAŻDY SKLADNIK MA SWOJĄ CENĘ!

"""
from abc import ABC, abstractmethod


class Component(ABC):

    @abstractmethod
    def get_cost(self) -> float:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass


class Price(ABC):

    def __init__(self, price: float):
        self._price = price

    @property
    def price(self):
        return self._price


class Description(ABC):

    def __init__(self, description: str):
        self._description = description

    @property
    def description(self):
        return self._description


class PlainPizza(Component):
    _PRICE = 15.0
    _DESCRIPTION = "Plain pizza"

    def get_cost(self) -> float:
        return self._PRICE

    def get_description(self) -> str:
        return self._DESCRIPTION


class PizzaAddition(Component, Price, Description):
    _PRICE = 0.0
    _DESCRIPTION = ''

    def __init__(self, addition: Component):
        # super().__init__(self._PRICE)
        Price.__init__(self, self._PRICE)
        Description.__init__(self, self._DESCRIPTION)

        self._wrappee = addition

    def get_cost(self) -> float:
        return self.price + self._wrappee.get_cost()

    def get_description(self) -> str:
        return f'{self._wrappee.get_description()}, {self.description}'


class Mozzarella(PizzaAddition):
    _PRICE = 10.0
    _DESCRIPTION = "Mozzarella"


class Ham(PizzaAddition):
    _PRICE = 5.0
    _DESCRIPTION = "Ham"


class Mushrooms(PizzaAddition):
    _PRICE = 5.0
    _DESCRIPTION = "Mushrooms"


class Salami(PizzaAddition):
    _PRICE = 5.0
    _DESCRIPTION = "Salami"


if __name__ == '__main__':
    pizza = PlainPizza()

    print(pizza.get_cost())
    print(pizza.get_description())

    pizza_with_mozzarella = Mozzarella(pizza)
    pizza_with_mozzarella_and_ham = Ham(pizza_with_mozzarella)

    print(pizza_with_mozzarella.get_cost())
    print(pizza_with_mozzarella.get_description())

    print(pizza_with_mozzarella_and_ham.get_cost())
    print(pizza_with_mozzarella_and_ham.get_description())
