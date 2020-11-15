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
    _PRICE = 0.0
    _DESCRIPTION = ""

    @abstractmethod
    def get_cost(self) -> float:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass


class PlainPizza(Component):

    _PRICE = 15.0
    _DESCRIPTION = "Plain pizza"

    def get_cost(self) -> float:
        return self._PRICE

    def get_description(self) -> str:
        return self._DESCRIPTION


class PizzaAddition(Component):

    def get_cost(self) -> float:
        return self._wrappee.get_cost() + self._PRICE

    def get_description(self) -> str:
        return f'{self._wrappee.get_description()}, {self._DESCRIPTION}'

    def __init__(self, addition: Component):
        self._wrappee = addition


class Mozzarella(PizzaAddition):
    _PRICE = 10.0
    _DESCRIPTION = "Mozzarella"

    def get_cost(self) -> float:
        return super().get_cost()

    def get_description(self) -> str:
        return super().get_description()


class Ham(PizzaAddition):
    _PRICE = 5.0
    _DESCRIPTION = "Ham"

    def get_cost(self) -> float:
        return super().get_cost()

    def get_description(self) -> str:
        return super().get_description()


class Mushrooms(PizzaAddition):
    _PRICE = 5.0
    _DESCRIPTION = "Mushrooms"

    def get_cost(self) -> float:
        return super().get_cost() + self._PRICE

    def get_description(self) -> str:
        return f'{self._DESCRIPTION}, {super().get_description()}'


class Salami(PizzaAddition):
    _PRICE = 5.0
    _DESCRIPTION = "Salami"

    def get_cost(self) -> float:
        return super().get_cost() + self._PRICE

    def get_description(self) -> str:
        return f'{self._DESCRIPTION}, {super().get_description()}'


if __name__ == '__main__':
    pizza = PlainPizza()

    print(pizza.get_cost())
    print(pizza.get_description())

    pizza_with_mozzarella = Mozzarella(pizza)

    print(pizza_with_mozzarella.get_cost())
    print(pizza_with_mozzarella.get_description())











