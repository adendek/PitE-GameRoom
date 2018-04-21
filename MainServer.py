#MainServer
#Authors Mario Carricato & Marco Amato

import socket  # Import socket module
from Utility.Player import Player
from Servers.ServerTicTacToe import ServerTicTacToe
from Servers.ServerGuessNumber import ServerGuessNumber
from Utility.Common import GamesType
from Utility.Common import PlayerType
from Utility.Common import ServerState
from Utility.Common import ServerEvent
from Utility.Transition import Transition

import time

PORT = 9999  # Reserve a port for your service.
HOST = socket.gethostbyname(socket.gethostname())  # Get local ip name

class MainServer:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((HOST, PORT))
        self.server_socket.listen(5)
        self.players = []
        self.game_mode = 0
        self.is_game_ended = False
        self.list_of_servers = [ServerTicTacToe(), ServerGuessNumber()]
        self.server_current_state = ServerState.LISTEN
        self.transitions = [
            Transition(ServerState.LISTEN, ServerEvent.WAIT_PLAYER, ServerState.LISTEN, self.start_server),
            Transition(ServerState.LISTEN, ServerEvent.START_MATCH, ServerState.CONNECTED, self.start_match),
            Transition(ServerState.CONNECTED, ServerEvent.FINISH_MATCH, ServerState.REFRESH, self.reinit_server),
            Transition(ServerState.REFRESH, ServerEvent.END_REINIT, ServerState.LISTEN, self.start_server)
        ]

    def start_match(self):
        for server in self.list_of_servers:
            if server.get_type_of_server() == int(self.game_mode):
                server.set_players(self.players)
                self.is_game_ended=server.start_game()


        if self.is_game_ended:
            self.manager_server_state(ServerEvent.FINISH_MATCH)

    def reinit_server(self):
        self.players.clear()
        self.game_mode = 0
        self.is_game_ended = False
        self.manager_server_state(ServerEvent.END_REINIT)

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

                message = "At the moment the server is hosting a "
                game_message = ""

                if self.game_mode == GamesType.TicTacToe.value:
                    game_message = "tic tac toe game "
                    player.set_symbol("\033[38;5;14mO\033[0m")
                elif self.game_mode == GamesType.GuessNumber.value:
                    game_message = "guess a number game "

                player.get_connection().send(
                    (message + game_message + "\nIf you want to join " + self.players[
                        PlayerType.Player1.value].get_name() + " insert " + str(self.game_mode)).encode())

                game_mode_choice = int(player.get_connection().recv(1024).decode())

                if game_mode_choice == self.game_mode:
                    player.get_connection().send(("Prepare for the match " + str(player.get_name())).encode())
                    self.players.append(player)
                    time.sleep(2)
                else:
                    player.get_connection().close()

            else:
                player.get_connection().send(
                    ("Please choose a game :\n1 for Tic Tac Toe \n2 for Guess a number \n ").encode())

                self.game_mode = int(player.get_connection().recv(1024).decode())

                if (self.game_mode == GamesType.TicTacToe.value):
                    player.set_symbol("\033[38;5;11mX\033[0m")

                player.get_connection().send(
                    ("Prepare for the match " + str(player.get_name()) + "\nWaiting for opponents").encode())

                self.players.append(player)

            if len(self.players) == 2:
                self.manager_server_state(ServerEvent.START_MATCH)


    def manager_server_state(self, event):
        print("MANAGER_STATES")
        for transition in self.transitions:
            if transition.event == event and self.server_current_state == transition.give_state:
                print("CURRENT STATE  ===> ",self.server_current_state)
                print("NEXT STATE     ===> ", transition.next_state,"\n\n")
                self.server_current_state = transition.next_state
                transition.action()



if __name__ == '__main__':
    server = MainServer()
    server.manager_server_state(ServerEvent.WAIT_PLAYER)


