#ClientTicTacToe
#Authors Mario Carricato & Marco Amato

import socket
import json
import os
from TicTacToe.Grid import Grid
from TicTacToe.Tic_tac_toe_game import start_Tic_Tac_Toe_game

#MOVES
LEFT = "4"
CENTER = "5"
RIGHT = "6"
UP = "8"
DOWN = "2"
UP_LEFT_CORNER = "7"
UP_RIGHT_CORNER = "9"
DOWN_LEFT_CORNER = "1"
DOWN_RIGHT_CORNER = "3"


class ClientTicTacToe:
    def __init__(self):
        self.client_socket = None
        self.grid = Grid()

    def set_client_socket(self,client_socket):
        self.client_socket = client_socket

    def start_client(self):
        print("waiting for server connection...")

        init = self.client_socket.recv(1024)
        print(init.decode())
        self.client_socket.send(str(input()).encode())

        data = self.client_socket.recv(1024)
        print(data.decode())

        self.client_socket.send(str(input()).encode())

        data = self.client_socket.recv(1024)
        print(data.decode())

        welcome_message = self.client_socket.recv(1024)
        print(welcome_message.decode())

        is_game_ended = False

        while not is_game_ended:
            response = self.client_socket.recv(1024)

            try:
                json_object = json.loads(response.decode())
                type_message = json_object.get("type")
                grid_list = json_object.get("grid")

                if type_message == 1:
                    valid_input = False
                    os.system("clear")
                    self.grid.draw_grid(grid_list)
                    name = json_object.get("name")
                    message = json_object.get("message")
                    print("\n"+name + " " + message+"\n")

                    while not valid_input:
                        player_choice = input()
                        if player_choice in [LEFT, RIGHT, CENTER, UP, DOWN, UP_LEFT_CORNER, UP_RIGHT_CORNER, DOWN_LEFT_CORNER, DOWN_RIGHT_CORNER]:
                            valid_input = True
                            self.client_socket.send(player_choice.encode())
                        else:
                            os.system("clear")
                            self.grid.draw_grid(grid_list)
                            print("\nyou have inserted invalid input")
                            print("Try Again")

                elif type_message == 2:
                    os.system("clear")
                    self.grid.draw_grid(grid_list)
                    message = json_object.get("message")
                    print("\n"+message)
                    is_game_ended = True

                else:
                    os.system("clear")
                    self.grid.draw_grid(grid_list)
                    message = json_object.get("message")
                    print("\n" + message)

            except:
                print('bad json')