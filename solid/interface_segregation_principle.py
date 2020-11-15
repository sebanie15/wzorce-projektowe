from abc import ABC, abstractmethod


class ProductActionsInterface(ABC):

    @abstractmethod
    def show_reviews(self):
        pass


class ComputerActionInterface(ProductActionsInterface, ABC):

    @abstractmethod
    def find_in_outlet(self):
        pass


class SoftwareActionInterface(ProductActionsInterface, ABC):

    @abstractmethod
    def try_for_seven_days(self):
        pass


class ComputerActionsUI(ComputerActionInterface):

    def show_reviews(self):
        pass

    def find_in_outlet(self):
        pass


class SoftwareActionsUI(ProductActionsInterface):

    def show_reviews(self):
        pass

    def try_for_seven_days(self):
        pass


"""
rozdzielic na interfejsy ComputerActionInterface(ProductActionsInterface, ABC) oraz SoftwareActionInterface(ProductActionsInterface, ABC)

w ProductActionsInterface(ABC) pozostawić tylko show_reviews
"""
