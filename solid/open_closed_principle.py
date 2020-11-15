from abc import ABC, abstractmethod


class Discount(ABC):
    _DISCOUNT = '20%'

    @abstractmethod
    def get_discount(self):
        return f'{self._DISCOUNT} on Easter'


class EasterDiscount(Discount):
    _EASTER_DISCOUNT = '30%'

    def get_discount(self):
        return f'{self._EASTER_DISCOUNT} on Easter'


class BlackFridayDiscount(Discount):
    _BLACK_FRIDAY_DISCOUNT = '50%'

    def get_discount(self):
        return f'{self._BLACK_FRIDAY_DISCOUNT} on Black Friday'


class BackToSchoolDiscount(Discount):
    _DISCOUNT = '20%'

    def get_discount(self):
        return f'{self._DISCOUNT} on Easter'


class DiscountManager:

    @staticmethod
    def process_discount(discount: Discount):
        discount.get_discount()


if __name__ == '__main__':
    discount_manager = DiscountManager()
    discount_manager.process_discount(EasterDiscount())
