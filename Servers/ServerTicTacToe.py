#ServerTicTacToe
#Authors Mario Carricato & Marco Amato

from TicTacToe.Grid import Grid
import time
import json
from Servers.FactoryServer import AbstractServer
from Common import GamesType
from Common import PlayerType
from Common import MessageType


class ServerTicTacToe(AbstractServer):

    def __init__(self):
        self.players = []
        self.grid = Grid()
        self.player_winner = ""
        self.draw = False
        self.type_of_server = GamesType.TicTacToe.value

    def get_type_of_server(self):
        return self.type_of_server

    def set_players(self, players):
        self.players = players

    def send_request(self, message, player, type):
        json_data = json.dumps(
            {"grid": self.grid.list, "message": message, "name": self.players[player].get_name(), "type": type})
        self.players[player].get_connection().send(json_data.encode())

    def check_victory(self, player):
        if self.grid.is_winner_player(player.get_symbol()):
            print("\n")
            print("\033[31;1mResult:\033[0m " + player.get_name() + " wins")
            print("\n")
            self.player_winner = player.get_name()
            return True
        else:
            return False

    def check_draw(self, moves_number):
        if self.grid.is_grid_full(moves_number):
            self.draw = True
            return self.draw
        else:
            return self.draw

    def start_game(self):

        is_game_ended = False

        welcome_message = "***** START MATCH *****\n" + \
                          self.players[PlayerType.Player1.value].get_name() + " VS " + self.players[
                              PlayerType.Player2.value].get_name() + "\n" + \
                          self.players[PlayerType.Player1.value].get_name() + " will play with symbol " + self.players[
                              PlayerType.Player1.value].get_symbol() + "\n" + \
                          self.players[PlayerType.Player2.value].get_name() + " will play with symbol " + self.players[
                              PlayerType.Player2.value].get_symbol() + "\n"

        print(welcome_message)

        self.players[PlayerType.Player1.value].get_connection().send(welcome_message.encode())
        self.players[PlayerType.Player2.value].get_connection().send(welcome_message.encode())

        time.sleep(4)

        message_not_empty = "sorry this cell is not empty.\nChoose another one:"
        message_turn = "it's your turn\nPlease make your choice : "

        moves_number = 0
        while not is_game_ended:

            self.send_request(message_turn, PlayerType.Player1.value, MessageType.MOVE_REQUEST.value)
            time.sleep(2)
            self.send_request("", PlayerType.Player2.value, MessageType.UPDATE_GUI.value)

            choice_check = True

            while choice_check:

                choice = int((self.players[PlayerType.Player1.value].get_connection().recv(1024).decode()))

                if self.grid.list[choice] != self.players[PlayerType.Player1.value].get_symbol() and self.grid.list[choice] != \
                        self.players[PlayerType.Player2.value].get_symbol():
                    self.grid.list[choice] = self.players[PlayerType.Player1.value].get_symbol()
                    moves_number += 1
                    self.send_request("", PlayerType.Player1.value, MessageType.UPDATE_GUI.value)
                    choice_check = False
                else:

                    self.send_request(message_not_empty, PlayerType.Player1.value, MessageType.MOVE_REQUEST.value)

            if self.check_victory(self.players[PlayerType.Player1.value]) or self.check_draw(moves_number):
                is_game_ended = True

            if not is_game_ended:

                self.send_request(message_turn, PlayerType.Player2.value, MessageType.MOVE_REQUEST.value)

                choice_check = True

                while choice_check:

                    choice = int((self.players[PlayerType.Player2.value].get_connection().recv(1024).decode()))

                    if self.grid.list[choice] != self.players[PlayerType.Player1.value].get_symbol() and self.grid.list[
                        choice] != self.players[PlayerType.Player2.value].get_symbol():
                        self.grid.list[choice] = self.players[PlayerType.Player2.value].get_symbol()
                        moves_number += 1
                        self.send_request("", PlayerType.Player2.value, MessageType.UPDATE_GUI.value)
                        choice_check = False
                    else:
                        message = "sorry this cell is not empty.\nChoose another one:"
                        self.send_request(message_not_empty, PlayerType.Player2.value, MessageType.MOVE_REQUEST.value)
                        time.sleep(1)

                if self.check_victory(self.players[PlayerType.Player2.value]) or self.check_draw(moves_number):
                    is_game_ended = True

        if not self.draw:
            message_winner = "\033[92mCongratulations, you won the game!!!\033[0m \n"
            message_loser = "\033[31;1mYou Lose...\033[0m\n"

            if self.player_winner == self.players[PlayerType.Player1.value].get_name():
                self.send_request(message_winner, PlayerType.Player1.value, MessageType.END_GAME.value)
                self.send_request(message_loser, PlayerType.Player2.value, MessageType.END_GAME.value)
            else:
                self.send_request(message_winner, PlayerType.Player2.value, MessageType.END_GAME.value)
                self.send_request(message_loser, PlayerType.Player1.value, MessageType.END_GAME.value)
        else:
            message_draw = "\033[38;5;13mThe Match terminates with a Draw!!!\033[0m\n"
            self.send_request(message_draw, PlayerType.Player1.value, MessageType.END_GAME.value)
            self.send_request(message_draw, PlayerType.Player2.value, MessageType.END_GAME.value)

