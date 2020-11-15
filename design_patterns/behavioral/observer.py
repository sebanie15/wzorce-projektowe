from abc import ABC, abstractmethod
from typing import List


class Subscriber(ABC):

    @abstractmethod
    def update(self, context):
        pass


class ConcreteSubscriber(Subscriber):

    def __init__(self, name):
        self._name = name

    def update(self, context):
        print(f'Subscriber {self._name} has been notified with result: {context.main_state}')
        # do some stuff...


class Publisher:
    def __init__(self):
        self._subscribers: List[Subscriber] = []
        self.main_state = False

    def subscribe(self, subscriber: Subscriber):
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber):
        self._subscribers.remove(subscriber)

    def notify_subscribers(self):
        for subscriber in self._subscribers:
            subscriber.update(self)

    def main_publisher_logic(self):
        # e.g. some calculations
        self.main_state = True
        self.notify_subscribers()


if __name__ == '__main__':
    publisher = Publisher()

    luke_subscriber = ConcreteSubscriber('Luke')
    publisher.subscribe(luke_subscriber)

    anakin_subscriber = ConcreteSubscriber('Anakin')
    publisher.subscribe(anakin_subscriber)

    publisher.main_publisher_logic()


# publisher -> leia_publisher żeby się utrzymać w motywie Star Wars
