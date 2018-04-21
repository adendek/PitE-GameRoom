# GuessNumber
# Authors Mario Carricato & Marco Amato

import random
import time
import os
from Utility.Player import Player

player = Player()


def generate_win_number():
    winner_number = random.randint(1, 100)
    return winner_number


def choice_number_to_low(number):
    number = str(number)
    col_number = "\033[38;5;14m" + number + "\033[0m"
    os.system("clear")
    number_to_low = "\n"+"  Oh NO... number : "+ col_number +" is too LOW \n" +"▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n████▌▄▌▄▐▐▌█████\n████▌▄▌▄▐▐▌▀████\n▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\n"
    return number_to_low


def choice_number_to_hight(number):
    number=str(number)
    col_number = "\033[38;5;14m"+number+"\033[0m"
    os.system("clear")
    print("\n")
    number_to_high = "\n" + "  Oh NO... number : " + col_number + " is too HIGH \n" + "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n████▌▄▌▄▐▐▌█████\n████▌▄▌▄▐▐▌▀████\n▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\n"
    return number_to_high


def choice_number_win(number, name):
    number = str(number)
    col_number = "\033[38;5;14m"+number+"\033[0m"
    col_name = "\033[38;5;11m"+name+"\033[0m"
    os.system("clear")
    you_win = "\n" + col_name + " with number : "+col_number +" YOU WIN \n" + "\n________$$$$\n    ___$$__$\n_______$___$$\n_______$___$$\n_______$$___$$\n________$____$$\n________$$____$$$\n_________$$_____$$\n_________$$______$$\n__________$_______$$\n____$$$$$$$________$$\n__$$$_______________$$$$$$\n_$$____$$$$____________$$$\n_$___$$$__$$$____________$$\n_$$________$$$____________$\n__$$____$$$$$$____________$\n__$$$$$$$____$$___________$\n__$$_______$$$$___________$\n___$$$$$$$$$__$$_________$$\n____$________$$$$_____$$$$\n____$$____$$$$$$____$$$$$$\n_____$$$$$$____$$__$$\n_______$_____$$$_$$$\n________$$$$$$$$$$\n"
    return you_win


def you_lose_match(name):
    colored_name = "\033[38;5;11m" + name + "\033[0m"
    os.system("clear")
    you_lose = "\n" + colored_name +"                _                  \n _   _  ___  _   _| |    ___  ___  ___\n| | | |/ _ \| | | | |   / _ \/ __|/ _ \ \n| |_| | (_) | |_| | |__| (_) \__ \  __/\n \__, |\___/ \__,_|_____\___/|___/\___|\n |___/\n"
    return you_lose


def check_attempts(number_of_attempts, name):
    if number_of_attempts > 4 and 4 < number_of_attempts < 7:
        print(name + " you still have few chance ...")
    if number_of_attempts == 7:
        print(name + " this your last chance... Good luck Man ")


def game_logic(win, name, number_to_guess):
    is_choice_wrong = True

    while is_choice_wrong:

        print("\n")
        input_choice = input("please insert your lucky number (1/100) ---> ")
        if input_choice.isdigit():
            choice = int(input_choice)
            if choice < 101:
                is_choice_wrong = False

                if choice > number_to_guess:
                    print(choice_number_to_hight(choice))

                elif choice < number_to_guess:
                    print(choice_number_to_low(choice))

                if choice == number_to_guess:
                    win = True
                    print(choice_number_win(choice, name))
                    return win
            else:
                print("Invalid input")
                time.sleep(0.5)

        else:
            print("Invalid input")
            time.sleep(0.5)

    return win


def start_guess_the_number():
    win = False
    number_of_attempts = 0
    print("\nHello player, you are welcome....")
    player.insert_player_name(input("Insert Your Name \n"))
    number_to_guess = generate_win_number()
    print(number_to_guess)
    name = player.get_name()

    while number_of_attempts < 8 and not win :
        check_attempts(number_of_attempts,name)

        win = game_logic(win, name, number_to_guess)
        number_of_attempts += 1

    if not win:
        print(you_lose_match(name))