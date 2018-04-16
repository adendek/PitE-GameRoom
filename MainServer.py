#MainServer
#Authors Mario Carricato & Marco Amato

import socket  # Import socket module
from Player import Player
from Servers.ServerTicTacToe import ServerTicTacToe
from Servers.ServerGuessNumber import ServerGuessNumber
import json
import time

PORT = 9999 # Reserve a port for your service.
HOST = socket.gethostbyname(socket.gethostname())  # Get local ip name

#CODES for 2 servers
TIC_TAC_TOE = 0
GUESS_NUMBER = 1

# players index of Server list
PLAYER_1 = 0
PLAYER_2 = 1



class MainServer:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((HOST, PORT))
        self.server_socket.listen(5)
        self.players = []
        self.game_mode = 0


    def start_server(self):

        print('Server listening.')
        print(HOST)

        while True:

            connection, address = self.server_socket.accept()
            print('Got connection from', address)
            player = Player()
            player.init_player("", address, connection)

            player.get_connection().send(
                ("Welcome " + str(player.get_address()) + "\nPlease insert your name").encode())

            player.set_name(player.get_connection().recv(1024).decode())

            if len(self.players) >= 1:
                player.set_symbol("\033[38;5;14mO\033[0m")

                message = "At the moment the server is hosting a "
                game_message = ""

                if self.game_mode == TIC_TAC_TOE:
                    game_message = "tic tac toe game "
                else :
                    game_message = "guess a number game "



                player.get_connection().send(
                    (message+game_message +"\nIf you want to join "+ self.players[PLAYER_1].get_name()+" insert "+str(self.game_mode)).encode())

                game_mode_choice = int(player.get_connection().recv(1024).decode())

                if game_mode_choice == self.game_mode:
                    player.get_connection().send(("Prepare for the match " + str(player.get_name())).encode())
                    self.players.append(player)
                    time.sleep(2)
                else :
                    player.get_connection().close()

            else:
                player.set_symbol("\033[38;5;11mX\033[0m")

                player.get_connection().send(
                    ("Please choose a game :\n0 for Tic Tac Toe \n1 for Guess a number \n ").encode())

                self.game_mode = int(player.get_connection().recv(1024).decode())

                player.get_connection().send(
                    ("Prepare for the match " + str(player.get_name()) + "\nWaiting for opponents").encode())

                self.players.append(player)


            if len(self.players) == 2:
                if self.game_mode == TIC_TAC_TOE :
                    tic_tac_toe_game = ServerTicTacToe()
                    tic_tac_toe_game.set_players(self.players)
                    tic_tac_toe_game.start_game()
                else :
                    guess_game = ServerGuessNumber()
                    guess_game.set_players(self.players)
                    guess_game.start_game()


MainServer().start_server()
