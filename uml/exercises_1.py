
class Animal:
    def __init__(self, age: int, gender: str) -> None:
        self.age = age
        self.gender = gender

    def is_mammal(self) -> bool:
        pass


class Dog(Animal):
    def __init__(self, age: int, gender: str, color: str) -> None:
        super().__init__(age, gender)
        self.color = color

    def bark(self) -> None:
        print("Hau hau")

    def fetch(self) -> None:
        pass


class Zebra(Animal):
    def __init__(self, age: int, gender: str, is_wild: bool) -> None:
        super().__init__(age, gender)
        self.is_wild = is_wild

    def run(self) -> None:
        print('I am running!')


class Duck(Animal):
    def __init__(self, age: int, gender: str, beak_color: str = 'yelow') -> None:
        super().__init__(age, gender)
        self._beak_color = beak_color

    def swim(self) -> None:
        print("i'm swimming...")

    def fly(self) -> None:
        print("I'm flying..")

    def quack(self) -> None:
        print("Quack")
