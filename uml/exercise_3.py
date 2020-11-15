from abc import ABC
from typing import List


class Acount:

    def __init__(self):
        self._balance: float = 0.0

    def deposit(self, amount: float):
        """

        :param amount:
        :return:
        """
        self._balance += amount

    def withdraw(self, amount: float):
        """

        :param amount:
        :return:
        """
        if amount <= self._balance:
            self._balance -= amount
        else:
            pass  # TODO - rise some error or withdraw(self._balance)

    def get_balance(self) -> float:
        """

        :return:
        """
        return self._balance


class AcountHolder(ABC):

    def __init__(self, id: int, email: str):
        self._email = email
        self._id = id
        self._acounts = List[Acount]


class IndividualHolder(AcountHolder):

    def __init__(self, id: int, email: str, name: str, pesel: str):
        super().__init__(id, email)
        self._pesel = pesel
        self._name = name


class CorporateHolder(AcountHolder):

    def __init__(self, id: int, email: str, contact: str):
        super().__init__(id, email)
        self._contact = contact
