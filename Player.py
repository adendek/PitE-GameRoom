#Player
#Authors Mario Carricato & Marco Amato

import socket

class Player:
    def __init__(self):
        self.name = ""
        self.address = ()
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.symbol = ""

    def set_connection(self, connection):
        self.connection =connection

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_symbol(self, symbol):
        self.symbol = symbol

    def get_connection(self):
        return self.connection

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_symbol(self):
        return self.symbol

    def get_player_name(self):
        return self.name

    def get_player_symbol(self):
        return self.symbol

    def init_player(self, name, address, connection):
        self.set_name(name)
        self.set_address(address)
        self.set_connection(connection)

    def insert_player_name(self):
        print("\nHello player, you are welcome....")
        self.name = input("Insert Your Name \n")

