#ServerTicTacToe
#Authors Mario Carricato & Marco Amato

from TicTacToe.Grid import Grid
import time
import json

# players index of Server list
PLAYER_1 = 0
PLAYER_2 = 1

# messages types codes
UPDATE_GUI = 0
MOVE_REQUEST = 1
END_GAME = 2


class ServerTicTacToe:

    def __init__(self):
        self.players = []
        self.grid = Grid()
        self.player_winner = ""
        self.draw = False

    def set_players(self,players):
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
                          self.players[PLAYER_1].get_name() + " VS " + self.players[
                              PLAYER_2].get_name() + "\n" + \
                          self.players[PLAYER_1].get_name() + " will play with symbol " + self.players[
                              PLAYER_1].get_symbol() + "\n" + \
                          self.players[PLAYER_2].get_name() + " will play with symbol " + self.players[
                              PLAYER_2].get_symbol() + "\n"

        print(welcome_message)

        self.players[PLAYER_1].get_connection().send(welcome_message.encode())
        self.players[PLAYER_2].get_connection().send(welcome_message.encode())

        time.sleep(4)

        message_not_empty = "sorry this cell is not empty.\nChoose another one:"
        message_turn = "it's your turn\nPlease make your choice : "

        moves_number = 0
        while not is_game_ended:

            self.send_request(message_turn, PLAYER_1, MOVE_REQUEST)
            self.send_request("", PLAYER_2, UPDATE_GUI)

            choice_check = True

            while choice_check:

                choice = int((self.players[PLAYER_1].get_connection().recv(1024).decode()))

                if self.grid.list[choice] != self.players[PLAYER_1].get_symbol() and self.grid.list[choice] != \
                        self.players[PLAYER_2].get_symbol():
                    self.grid.list[choice] = self.players[PLAYER_1].get_symbol()
                    moves_number += 1
                    self.send_request("", PLAYER_1, UPDATE_GUI)
                    choice_check = False
                else:

                    self.send_request(message_not_empty, PLAYER_1, MOVE_REQUEST)

            if self.check_victory(self.players[PLAYER_1]) or self.check_draw(moves_number):
                is_game_ended = True

            if not is_game_ended:

                self.send_request(message_turn, PLAYER_2, MOVE_REQUEST)

                choice_check = True

                while choice_check:

                    choice = int((self.players[PLAYER_2].get_connection().recv(1024).decode()))

                    if self.grid.list[choice] != self.players[PLAYER_1].get_symbol() and self.grid.list[
                        choice] != self.players[PLAYER_2].get_symbol():
                        self.grid.list[choice] = self.players[PLAYER_2].get_symbol()
                        moves_number += 1
                        self.send_request("", PLAYER_2, UPDATE_GUI)
                        choice_check = False
                    else:
                        message = "sorry this cell is not empty.\nChoose another one:"
                        self.send_request(message_not_empty, PLAYER_2, MOVE_REQUEST)
                        time.sleep(1)

                if self.check_victory(self.players[PLAYER_2]) or self.check_draw(moves_number):
                    is_game_ended = True

        if not self.draw:
            message_winner = "\033[92mCongratulations, you won the game!!!\033[0m \n"
            message_loser = "\033[31;1mYou Lose...\033[0m\n"

            if self.player_winner == self.players[PLAYER_1].get_name():
                self.send_request(message_winner, PLAYER_1, END_GAME)
                self.send_request(message_loser, PLAYER_2, END_GAME)
            else:
                self.send_request(message_winner, PLAYER_2, END_GAME)
                self.send_request(message_loser, PLAYER_1, END_GAME)
        else:
            message_draw = "\033[38;5;13mThe Match terminates with a Draw!!!\033[0m\n"
            self.send_request(message_draw, PLAYER_1, END_GAME)
            self.send_request(message_draw, PLAYER_2, END_GAME)

