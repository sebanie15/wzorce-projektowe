from abc import ABC, abstractmethod
from typing import List, Optional


class Component(ABC):
    @abstractmethod
    def execute(self):
        pass


class Hammer(Component):
    def __init__(self, name):
        self._name = name

    def execute(self):
        print(f'{self._name} - Hammer operation')


class Charger(Component):
    def __init__(self, name):
        self._name = name

    def execute(self):
        print(f'{self._name} - Charger operation')


class Composite(Component):

    def __init__(self):
        self._children: Optional[List[Component]] = []

    def add(self, component: Component):
        self._children.append(component)

    def remove(self, component: Component):
        self._children.remove(component)

    def get_children(self):
        return self._children

    def execute(self):
        for child in self._children:
            child.execute()


if __name__ == '__main__':
    composite = Composite()
    composite.add(Hammer('1'))
    composite.add(Hammer('2'))
    composite.add(Hammer('3'))
    # composite.execute()

    #               []
    #        []             []
    # <1>   <2>  <3>     <4>  (5)
    #

    mixed_composite = Composite()
    mixed_composite.add(Hammer('4'))
    mixed_composite.add(Charger('5'))

    parent_composite = Composite()
    parent_composite.add(composite)
    parent_composite.add(mixed_composite)
    parent_composite.execute()


    # parent_composite.add(Leaf('4'))
    # parent_composite.add(composite)
    # parent_composite.execute()
