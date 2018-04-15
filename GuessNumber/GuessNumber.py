#Tic_tac_toe_game
#Authors Mario Carricato & Marco Amato

import random
import time
import os
from Player import Player

player = Player()


def generate_win_number():
    winner_number = random.randint(1, 100)
    return winner_number


def choice_number_to_low(number):
    number = str(number)
    col_number = "\033[38;5;14m" + number + "\033[0m"
    os.system("clear")
    print("\n")
    print (" Oh NO... number : "+ col_number +" is too LOW \n")
    print("\n\
    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n\
    ████▌▄▌▄▐▐▌█████\n\
    ████▌▄▌▄▐▐▌▀████\n\
    ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\n")


def choice_number_to_hight(number):
    number=str(number)
    col_number = "\033[38;5;14m"+number+"\033[0m"
    os.system("clear")
    print("\n")
    print (" Oh NO... number : " +col_number +" is too HIGh\n")
    print("\n\
        ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n\
        ████▌▄▌▄▐▐▌█████\n\
        ████▌▄▌▄▐▐▌▀████\n\
        ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\n")


def choice_number_win(number, name):
    number = str(number)
    col_number = "\033[38;5;14m"+number+"\033[0m"
    col_name = "\033[38;5;11m"+name+"\033[0m"
    os.system("clear")
    print("\n")
    print (col_name + " with number : "+col_number +" YOU WIN \n")
    print("\n\
           ________$$$$\n\
                ___$$__$\n\
            _______$___$$\n\
            _______$___$$\n\
            _______$$___$$\n\
            ________$____$$\n\
            ________$$____$$$\n\
            _________$$_____$$\n\
            _________$$______$$\n\
            __________$_______$$\n\
            ____$$$$$$$________$$\n\
            __$$$_______________$$$$$$\n\
            _$$____$$$$____________$$$\n\
            _$___$$$__$$$____________$$\n\
            _$$________$$$____________$\n\
            __$$____$$$$$$____________$\n\
            __$$$$$$$____$$___________$\n\
            __$$_______$$$$___________$\n\
            ___$$$$$$$$$__$$_________$$\n\
            ____$________$$$$_____$$$$\n\
            ____$$____$$$$$$____$$$$$$\n\
            _____$$$$$$____$$__$$\n\
            _______$_____$$$_$$$\n\
            ________$$$$$$$$$$\n")


def you_lose_match(name):
    col_name = "\033[38;5;11m" + name + "\033[0m"
    os.system("clear")
    print("\n")
    print (col_name + " YOU LOSE \n")
    print("\n\
    ______________$$$$$$$$$$____________________\n\
    _____________$$__$_____$$$$$________________\n\
    _____________$$_$$__$$____$$$$$$$$__________\n\
    ____________$$_$$__$$$$$________$$$_________\n\
    ___________$$_$$__$$__$$_$$$__$$__$$________\n\
    ___________$$_$$__$__$$__$$$$$$$$__$$_______\n\
    ____________$$$$$_$$_$$$_$$$$$$$$_$$$_______\n\
    _____________$$$$$$$$$$$$$_$$___$_$$$$______\n\
    ________________$$_$$$______$$$$$_$$$$______\n\
    _________________$$$$_______$$$$$___$$$_____\n\
    ___________________________$$_$$____$$$$____\n\
    ___________________________$$_$$____$$$$$___\n\
    __________________________$$$$$_____$$$$$$__\n\
    _________________________$__$$_______$$$$$__\n\
    ________________________$$$_$$________$$$$$_\n\
    ________________________$$$___________$$$$$_\n\
    _________________$$$$___$$____________$$$$$$\n\
    __$$$$$$$$____$$$$$$$$$$_$____________$$$_$$\n\
    _$$$$$$$$$$$$$$$______$$$$$$$___$$____$$_$$$\n\
    $$________$$$$__________$_$$$___$$$_____$$$$\n\
    $$______$$$_____________$$$$$$$$$$$$$$$$$_$$\n\
    $$______$$_______________$$_$$$$$$$$$$$$$$$_\n\
    $$_____$_$$$$$__________$$$_$$$$$$$$$$$$$$$_\n\
    $$___$$$__$$$$$$$$$$$$$$$$$__$$$$$$$$$$$$$__\n\
    $$_$$$$_____$$$$$$$$$$$$________$$$$$$__$___\n\
    $$$$$$$$$$$$$$_________$$$$$______$$$$$$$___\n\
    $$$$_$$$$$______________$$$$$$$$$$$$$$$$____\n\
    $$__$$$$_____$$___________$$$$$$$$$$$$$_____\n\
    $$_$$$$$$$$$$$$____________$$$$$$$$$$_______\n\
    $$_$$$$$$$hg$$$____$$$$$$$$__$$$____________\n\
    $$$$__$$$$$$$$$$$$$$$$$$$$$$$$______________\n\
    $$_________$$$$$$$$$$$$$$$__________________\n")


def start_guess_the_number():
    win = False
    number_of_attempts = 0
    player.insert_player_name()
    number_to_guess = generate_win_number()
    print(number_to_guess)
    name = player.get_name()

    while number_of_attempts < 8:
        if number_of_attempts > 4 and number_of_attempts < 7 :
            print(name + " you still have few chance ...")
        if number_of_attempts == 7:
            print(name + " this your last chance... Good luck Man ")

        is_choice_wrong = True
        while is_choice_wrong:
            print("\n")
            input_choice = input("please insert your lucky number (1/100) ---> ")
            if input_choice.isdigit():
                choice = int(input_choice)
                if choice < 101:
                    is_choice_wrong = False

                    if choice > number_to_guess:
                        choice_number_to_hight(choice)
                        number_of_attempts = number_of_attempts + 1

                    elif choice < number_to_guess:
                        choice_number_to_low(choice)
                        number_of_attempts = number_of_attempts + 1

                    if choice == number_to_guess:
                        win = True
                        choice_number_win(choice, name)
                        return
                else:
                    print("Invalid input")
                    time.sleep(0.5)

            else:
                print("Invalid input")
                time.sleep(0.5)

    if not win:
        you_lose_match(name)
