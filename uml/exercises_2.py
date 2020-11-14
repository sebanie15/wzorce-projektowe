from abc import ABC, abstractmethod
from typing import List, Type, Optional


class Vehicle(ABC):

    def __init__(self, model: str, brand: str):
        self.brand = brand
        self.model = model

    @abstractmethod
    def is_dirty(self) -> bool:
        pass

    @abstractmethod
    def drive(self) -> bool:
        pass


class Car(Vehicle):

    def is_dirty(self) -> bool:
        pass

    def drive(self) -> bool:
        pass

    def __init__(self, model: str, brand: str, number_of_seats: int):
        super().__init__(model, brand)
        self.number_of_seats = number_of_seats

    def drive_on_holidays(self):
        pass


class Truck(Vehicle):

    def is_dirty(self) -> bool:
        pass

    def drive(self) -> bool:
        pass

    def __init__(self, model: str, brand: str, load: float):
        super().__init__(model, brand)
        self._load = load

    def deliver_cargo(self):
        pass


class CarWash:

    def __init__(self, price_list: List[str]):
        self.price_list = price_list

    def wash_vehicle(self, vehicle: Vehicle):
        pass

    def is_out_of_order(self) -> bool:
        pass


class Owner:

    def __init__(self):
        self._vehicle: Optional[Vehicle] = None

    def go_to_car_wash(self, car_wash: CarWash):
        pass

    def buy_new_vehicle(self, vehicle_type: Type[Vehicle]):
        pass
