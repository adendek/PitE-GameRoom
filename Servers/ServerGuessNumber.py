# ServerGuessNumber
# Authors Mario Carricato & Marco Amato

import json
from GuessNumber.GuessNumber import *
from Servers.FactoryServer import AbstractServer
from Utility.Common import GamesType
from Utility.Common import PlayerType
from Utility.Common import MessageType

class ServerGuessNumber(AbstractServer):

    def __init__(self):
        self.players = []
        self.player_winner = ""
        self.winner_number = 0
        self.number_to_guess = generate_win_number()
        self.draw = False
        self.number_of_attempts = [0, 0]
        self.type_of_server = GamesType.GuessNumber.value

    def get_type_of_server(self):
        return self.type_of_server

    def set_players(self, players):
        self.players = players

    def send_request(self, message, player, type):
        json_data = json.dumps(
            {"message": message, "name": self.players[player].get_name(), "type": type})
        self.players[player].get_connection().send(json_data.encode())

    def check_attempts(self,number_of_attempts, player):

        request_message = "\nplease insert your lucky number (1/100) ---> "

        if 4 < number_of_attempts < 7:
            message = " you still have few chance ..."+request_message
        elif number_of_attempts == 7:
            message = " this your last chance... Good luck Man "+request_message
        else :
            message = request_message

        self.send_request(message, player, MessageType.CHECK_ATTEMPTS.value)

    def main_logic(self, number, player):
        if number > self.number_to_guess:
            self.send_request(choice_number_to_hight(number), player, MessageType.RESPONSE.value)
            return False

        elif number < self.number_to_guess:
            self.send_request(choice_number_to_low(number), player, MessageType.RESPONSE.value)
            return False

        else:
            self.player_winner = self.players[player].get_name()
            self.winner_number = number
            return True

    def start_game(self):

        is_game_ended = False

        welcome_message = "***** START MATCH *****\n" + \
                          self.players[PlayerType.Player1.value].get_name() + " VS " + self.players[
                              PlayerType.Player2.value].get_name() + "\nLet's See who will guess my number Before"

        print(welcome_message)

        self.players[PlayerType.Player1.value].get_connection().send(welcome_message.encode())
        self.players[PlayerType.Player2.value].get_connection().send(welcome_message.encode())

        time.sleep(2)


        while not is_game_ended and (self.number_of_attempts[PlayerType.Player1.value] + self.number_of_attempts[PlayerType.Player2.value]) < 16 :

            print(self.number_to_guess)

            if self.number_of_attempts[PlayerType.Player1.value] <= 8  :

                self.check_attempts(self.number_of_attempts[PlayerType.Player1.value],PlayerType.Player1.value)

                number_player1 = int(self.players[PlayerType.Player1.value].get_connection().recv(1024).decode())

                is_game_ended = self.main_logic(number_player1, PlayerType.Player1.value)

                self.number_of_attempts[PlayerType.Player1.value] += 1

            if not is_game_ended and self.number_of_attempts[PlayerType.Player2.value] <= 8 :

                self.check_attempts(self.number_of_attempts[PlayerType.Player2.value], PlayerType.Player2.value)

                number_player2 = int(self.players[PlayerType.Player2.value].get_connection().recv(1024).decode())

                is_game_ended = self.main_logic(number_player2, PlayerType.Player2.value)

                self.number_of_attempts[PlayerType.Player2.value] += 1

        self.draw = not is_game_ended

        if not self.draw:

            if self.player_winner == self.players[PlayerType.Player1.value].get_name():
                self.send_request(choice_number_win(self.winner_number,self.players[PlayerType.Player1.value].get_name()), PlayerType.Player1.value, MessageType.END_GAME.value)
                self.send_request(you_lose_match(self.players[PlayerType.Player2.value].get_name()), PlayerType.Player2.value, MessageType.END_GAME.value)
            else:
                self.send_request(choice_number_win(self.winner_number,self.players[PlayerType.Player2.value].get_name()), PlayerType.Player2.value, MessageType.END_GAME.value)
                self.send_request(you_lose_match(self.players[PlayerType.Player1.value].get_name()), PlayerType.Player1.value, MessageType.END_GAME.value)
        else:
            self.send_request(you_lose_match(self.players[PlayerType.Player1.value].get_name()), PlayerType.Player1.value, MessageType.END_GAME.value)
            self.send_request(you_lose_match(self.players[PlayerType.Player2.value].get_name()), PlayerType.Player2.value, MessageType.END_GAME.value)

        return True