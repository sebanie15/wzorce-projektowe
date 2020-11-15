from abc import ABC, abstractmethod


class Product1:
    pass


class Product2:
    pass


class Builder(ABC):

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def build_step_1(self):
        pass

    @abstractmethod
    def build_step_2(self):
        pass


class ConcreteBuilder1(Builder):
    def __init__(self):
        self._result: Product1 = Product1()

    def reset(self):
        self._result = Product1()

    def build_step_1(self):
        print('Add garage!')

    def build_step_2(self):
        print('Add swimming')

    def get_result(self) -> Product1:
        return self._result


class ConcreteBuilder2(Builder):
    def __init__(self):
        self._result: Product2 = Product2()

    def reset(self):
        self._result = Product2()

    def build_step_1(self):
        pass

    def build_step_2(self):
        pass

    def get_result(self) -> Product2:
        return self._result


class Director:
    def __init__(self, builder: Builder):
        self._builder = builder

    def change_builder(self, builder: Builder):
        self._builder = builder

    def make(self, object_type=None):
        self._builder.reset()
        self._builder.build_step_1()
        if object_type == 'complex':
            self._builder.build_step_2()

    def another_make(self, object_type: list = None):
        self._builder.reset()
        self._builder.build_step_1()
        if 'complex' in object_type:
            self._builder.build_step_2()
        if 'another type' in object_type:
            pass


if __name__ == '__main__':
    builder = ConcreteBuilder1()
    director = Director(builder)
    director.make('complex')
    complex_product = builder.get_result()
    t = 0
