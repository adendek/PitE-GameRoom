import abc


class AbstractClient(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def set_client_socket(self, client_socket):
        pass

    @abc.abstractmethod
    def start_client(self):
        pass




