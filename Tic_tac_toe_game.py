#Tic_tac_toe_game 
#Authors Mario Carricato & Marco Amato

import time

from Grid import Grid
from Computer import Computer
from Player import Player

grid_obj = Grid()
computer = Computer()
player = Player()


def start_game():

    run = 0
    player.insert_player_name()

    while True:

        is_choice_wrong = True
        while is_choice_wrong:
            grid_obj.get_snapschoot()
            choice = input("chose an empty space for X. ")
            if choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                choice = int(choice)
                if grid_obj.list[choice] != "X" and grid_obj.list[choice] != "O":
                    grid_obj.list[choice] = "X"
                    run = run + 1
                    is_choice_wrong = False
                else:
                    print("sorry this cell is not empty. Choose another one")
                    time.sleep(1)
            else:
                print("Invalid input")
                time.sleep(1)

        if grid_obj.is_winner_player("X"):
            grid_obj.get_snapschoot()
            player_name = player.get_player_name()
            print ("\n")
            print ("\033[31;1mResult:\033[0m "+player_name + " wins")
            print ("\n")
            return "Player_Win"

        if grid_obj.is_grid_full(run):
            return "Draw"

        is_choice_wrong = True

        while is_choice_wrong:
            grid_obj.get_snapschoot()
            time.sleep(0.5)
            choice = computer.get_move_ai(grid_obj.list)

            if grid_obj.list[choice] != "O" and grid_obj.list[choice] != "X":
                grid_obj.list[choice] = "O"
                run = run + 1
                is_choice_wrong = False

        if grid_obj.is_winner_player("O"):
            grid_obj.get_snapschoot()
            print ("\n")
            print ("\033[31;1mResult:\033[0m Computer Wins ")
            print ("\n")
            return "Pc_Win"

        if grid_obj.is_grid_full(run):
            return "Draw"


if __name__ == '__main__':
    start_game()
