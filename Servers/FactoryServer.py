import abc


class AbstractServer(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def send_request(self, message, player, type):
        pass

    @abc.abstractmethod
    def start_game(self):
        pass

    @abc.abstractmethod
    def set_players(self, players):
        pass


