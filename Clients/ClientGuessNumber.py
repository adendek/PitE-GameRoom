#ClientTicTacToe
#Authors Mario Carricato & Marco Amato

import socket
import json
import os
import time

from Clients.FactoryClient import AbstractClient


class ClientGuessNumber(AbstractClient):
    def __init__(self):
        self.client_socket = None
        self.type_of_client = 1

    def get_type_of_client(self):
        return self.type_of_client

    def set_client_socket(self, client_socket):
        self.client_socket = client_socket

    def start_client(self):

        welcome_message = self.client_socket.recv(1024)
        print(welcome_message.decode())

        is_game_ended = False

        while not is_game_ended:

            response = self.client_socket.recv(1024)

            try:
                json_object = json.loads(response.decode())
                type_message = json_object.get("type")

                if type_message == 0:

                       is_choice_wrong = True
                       message = json_object.get("message")
                       while is_choice_wrong:

                        print("\n")
                        input_choice = input(message)
                        if input_choice.isdigit():
                            choice = int(input_choice)
                            if choice < 101:
                                is_choice_wrong = False

                                self.client_socket.send(str(choice).encode())

                            else:
                                print("Invalid input")
                                time.sleep(0.5)

                        else:
                            print("Invalid input")
                            time.sleep(0.5)

                elif type_message == 1:

                    os.system("clear")
                    message = json_object.get("message")
                    print("\n"+message)

                else:

                    os.system("clear")
                    message = json_object.get("message")
                    print("\n" + message)
                    is_game_ended = True

            except:
                print('Lost Connection..')
                break