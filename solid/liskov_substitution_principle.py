from abc import ABC, abstractmethod


class DeliveryBase(ABC):

    def __init__(self, product_ids, user):
        self.product_ids = product_ids
        self.user = user


class LocationDeliveryBase(DeliveryBase, ABC):

    @abstractmethod
    def get_delivery_location(self):
        pass


class OnlineDeliveryBase(DeliveryBase, ABC):

    @abstractmethod
    def get_email(self):
        pass


class ComputerDelivery(DeliveryBase):

    def get_delivery_location(self):
        pass


class SoftwareDelivery(OnlineDeliveryBase, LocationDeliveryBase):

    def get_delivery_location(self):
        pass

    def get_email(self):
        pass
