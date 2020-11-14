
"""
this is a module docstring
"""


class SamplePylint:  # pylint: disable=too-few-public-methods
    """this is a class SamplePaylint docstring"""

    def __init__(self, number: int):
        self._number = number

    @staticmethod
    def divide(number: int) -> None:
        """docstring for method divide

        Args:
            number: int

        Returns:
            None
        """
        if number == 0:
            raise ZeroDivisionError()


class Children(SamplePylint):  # pylint: disable=too-few-public-methods
    """this is a class Children docstring"""
    def __init__(self, number: int, name: str) -> None:
        super().__init__(number)
        self._name = name

    @staticmethod
    def some_method(param: int) -> bool:
        """this is a static method

        Args:
            param: int

        Returns:
            bool
        """
        save_digits = [1, 2, 3]
        return param in [1, 2, 3]

    @staticmethod
    def some_method_2() -> None:
        """this is some method with bad implementation

        Returns:
            None
        """
        print("bad implementation")


if __name__ == "__main__":
    sample = SamplePylint(10)
    try:
        sample.divide(0)
    except ZeroDivisionError:
        pass

    sample.divide(2)

    obj = Children(2, "name")
    print(obj.some_method(2))
