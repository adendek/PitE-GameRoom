#MainClient
#Authors Mario Carricato & Marco Amato

import socket
import json
import os
from TicTacToe.Tic_tac_toe_game import start_Tic_Tac_Toe_game
from GuessNumber.GuessNumber import start_guess_the_number
from Clients.ClientTicTacToe import ClientTicTacToe
from Clients.ClientGuessNumber import ClientGuessNumber

TIC_TAC_TOE = 0
GUESS_A_NUMBER = 1

class MainClient:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        self.client_socket.connect((HOST, PORT))

    def start_client(self):
        print("waiting for server connection...")

        #connection establishment
        init = self.client_socket.recv(1024)                    
        print(init.decode())
        #insert name
        self.client_socket.send(str(input()).encode())

        #request for a game mode
        request_game_mode = self.client_socket.recv(1024)
        print(request_game_mode.decode())

        #insert game mode
        while True:
            game_mode = str(input())
            if game_mode in [str(TIC_TAC_TOE), str(GUESS_A_NUMBER)]:
                self.client_socket.send(game_mode.encode())
                waiting_message = self.client_socket.recv(1024)
                print(waiting_message.decode())
                break
            else :
                print("you entered a wrong choice\nPlease choose a game :\n0 for Tic Tac Toe \n1 for Guess a number \n")




        if int(game_mode) == TIC_TAC_TOE :
            client_tic_tac_toe = ClientTicTacToe()
            client_tic_tac_toe.set_client_socket(self.client_socket)
            client_tic_tac_toe.start_client()
        else :
            client_guess_number = ClientGuessNumber()
            client_guess_number.set_client_socket(self.client_socket)
            client_guess_number.start_client()






print("\n")
print("************************************************")
print("*****               Game Room             ******")
print("************************************************")
print("*                                              *")
print("*               Play single player  --- s      *")
print("*                                              *")
print("*               Play multi player   --- m      *")
print("*                                              *")
print("************************************************")

while True:

    print("\n")
    choice = input("Please, choose one mode ( s or m ) ---->    ")
    print("\n")
    os.system("clear")


    if choice == "s":
        print("************************************************")
        print("*                                              *")
        print("*               Play tic tac toe      --- t    *")
        print("*                                              *")
        print("*               Play guess a number   --- g    *")
        print("*                                              *")
        print("************************************************")

        while True:

            choice = input("\nPlease, choose one game ( t or g ) ---->    ")
            print("\n")

            if choice == "t":
                start_Tic_Tac_Toe_game()
                break
            elif choice == "g":
                start_guess_the_number()
                break
            else :
                print("You entered wrong choice\n")

        break

    elif choice == "m":
        HOST = str(input("please insert ip address of the game server\n"))                     # HOST = "10.205.12.240"
        PORT = int(input("please insert Port number of the game server\n"))                    # PORT = 9999
        MainClient().start_client()

        break

    else:
        print("You entered wrong choice\n")

