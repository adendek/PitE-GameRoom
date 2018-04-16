# ServerGuessNumber
# Authors Mario Carricato & Marco Amato

import time
import json
from GuessNumber.GuessNumber import *

# players index of Server list
PLAYER_1 = 0
PLAYER_2 = 1

# messages types codes
CHECK_ATTEMPTS = 0
RESPONSE = 1
END_GAME = 2


class ServerGuessNumber:

    def __init__(self):
        self.players = []
        self.player_winner = ""
        self.winner_number = 0
        self.number_to_guess = generate_win_number()
        self.draw = False
        self.number_attempts = [0,0]

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

        self.send_request(message,player,CHECK_ATTEMPTS)


    def main_logic(self,number,player):

        if number > self.number_to_guess:
            self.send_request(choice_number_to_hight(number), player, RESPONSE)
            return False

        elif number < self.number_to_guess:
            self.send_request(choice_number_to_low(number), player, RESPONSE)
            return False

        else:
            self.player_winner = self.players[player].get_name()
            self.winner_number = number
            return True

    def start_game(self):

        is_game_ended = False

        welcome_message = "***** START MATCH *****\n" + \
                          self.players[PLAYER_1].get_name() + " VS " + self.players[
                              PLAYER_2].get_name() + "\nLet's See who will guess my number Before"

        print(welcome_message)

        self.players[PLAYER_1].get_connection().send(welcome_message.encode())
        self.players[PLAYER_2].get_connection().send(welcome_message.encode())

        time.sleep(4)

        while not is_game_ended and (self.number_of_attempts[PLAYER_1] + self.number_of_attempts[PLAYER_2]) < 16 :


            print(self.number_to_guess)


            if self.number_of_attempts[PLAYER_1] <= 8  :

                check_attempts(self.number_of_attempts[PLAYER_1],PLAYER_1)

                number_player1 = self.players[PLAYER_1].get_connection().recv(1024).decode()

                is_game_ended = self.main_logic(number_player1, PLAYER_1)

                self.number_of_attempts[PLAYER_1] += 1



            if not is_game_ended and self.number_of_attempts[PLAYER_2] <= 8 :

                check_attempts(self.number_of_attempts[PLAYER_2], PLAYER_2)

                number_player2 = self.players[PLAYER_2].get_connection().recv(1024).decode()

                is_game_ended = self.main_logic(number_player2, PLAYER_2)

                self.number_of_attempts[PLAYER_2] += 1




        self.draw = not is_game_ended




        if not self.draw:

            if self.player_winner == self.players[PLAYER_1].get_name():
                self.send_request(choice_number_win(self.winner_number,self.players[PLAYER_1].get_name()), PLAYER_1, END_GAME)
                self.send_request(you_lose_match(self.players[PLAYER_2].get_name()), PLAYER_2, END_GAME)
            else:
                self.send_request(choice_number_win(self.winner_number,self.players[PLAYER_2].get_name()), PLAYER_2, END_GAME)
                self.send_request(you_lose_match(self.players[PLAYER_1].get_name()), PLAYER_1, END_GAME)
        else:
            self.send_request(you_lose_match(self.players[PLAYER_1].get_name()), PLAYER_1, END_GAME)
            self.send_request(you_lose_match(self.players[PLAYER_2].get_name()), PLAYER_2, END_GAME)
