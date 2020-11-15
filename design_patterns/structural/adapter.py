from abc import ABC, abstractmethod


class Service:
    def service_method(self, data):
        # tu je przetwarza
        return 'response'


class ClientInterface(ABC):

    @abstractmethod
    def some_method(self, data):
        pass


class Adapter(ClientInterface):

    def __init__(self, adaptee: Service):
        self._adaptee = adaptee

    def _convert_to_service_format(self, data):
        # performs conversion
        return data

    def some_method(self, data):
        # some operations to convert data
        # e.g.:
        special_data = self._convert_to_service_format(data)
        return self._adaptee.service_method(special_data)


if __name__ == '__main__':
    service = Service()
    adapter = Adapter(service)

    data = {}
    service_response = adapter.some_method(data)

    new_data = Adapter(Service()).some_method(data)
