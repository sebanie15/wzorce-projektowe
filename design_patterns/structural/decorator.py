from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def execute(self):
        pass


class ConcreteComponent(Component):

    def execute(self):
        print('ConcreteComponent')


class BaseDecorator(Component):

    def __init__(self, component: Component):
        self._wrappee = component

    def execute(self):
        self._wrappee.execute()


class ConcreteDecorator1(BaseDecorator):

    def _extra(self):
        # some operation
        print('ConcreteDecorator1')

    def execute(self):
        self._extra()
        super().execute()


class ConcreteDecorator2(BaseDecorator):

    def _extra(self):
        # some another operation
        print('ConcreteDecorator2')

    def execute(self):
        self._extra()
        super().execute()


if __name__ == '__main__':
    component = ConcreteComponent()
    # component.execute()

    # decorator_1 = ConcreteDecorator1(component)
    # decorator_2 = ConcreteDecorator2(decorator_1)
    # decorator_2 = ConcreteDecorator2(decorator_2)
    # decorator_2.execute()


    concrete_component = ConcreteComponent()
    concrete_decorator_1 = ConcreteDecorator1(concrete_component)
    concrete_decorator_2 = ConcreteDecorator2(concrete_decorator_1)
    concrete_decorator_2.execute()

    # ConcreteDecorator2 -> ConcreteDecorator1 -> ConcreteComponent
