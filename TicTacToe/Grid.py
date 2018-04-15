#Grid
#Authors Mario Carricato & Marco Amato

import os

#positions
LEFT = 4
CENTER = 5
RIGHT = 6
UP = 8
DOWN = 2
UP_LEFT_CORNER = 7
UP_RIGHT_CORNER = 9
DOWN_LEFT_CORNER = 1
DOWN_RIGHT_CORNER = 3


class Grid:
    def __init__(self):
        self.list = ["", str(DOWN_LEFT_CORNER), str(DOWN), str(DOWN_RIGHT_CORNER), str(LEFT), str(CENTER), str(RIGHT), str(UP_LEFT_CORNER), str(UP), str(UP_RIGHT_CORNER)]

    def print_grid(self):
        print ("   |   |   ")
        print (" " + self.list[UP_LEFT_CORNER] + " | " + self.list[UP] + " | " + self.list[UP_RIGHT_CORNER] + "  ")
        print ("   |   |   ")
        print ("-----------")
        print ("   |   |   ")
        print (" " + self.list[LEFT] + " | " + self.list[CENTER] + " | " + self.list[RIGHT] + "  ")
        print ("   |   |   ")
        print ("-----------")
        print ("   |   |   ")
        print (" " + self.list[DOWN_LEFT_CORNER] + " | " + self.list[DOWN] + " | " + self.list[DOWN_RIGHT_CORNER] + "  ")
        print ("   |   |   ")

    def draw_grid(self, list):
        print ("   |   |   ")
        print (" " + list[UP_LEFT_CORNER] + " | " + list[UP] + " | " + list[UP_RIGHT_CORNER] + "  ")
        print ("   |   |   ")
        print ("-----------")
        print ("   |   |   ")
        print (" " + list[LEFT] + " | " + list[CENTER] + " | " + list[RIGHT] + "  ")
        print ("   |   |   ")
        print ("-----------")
        print ("   |   |   ")
        print (" " + list[DOWN_LEFT_CORNER] + " | " + list[DOWN] + " | " + list[DOWN_RIGHT_CORNER] + "  ")
        print ("   |   |   ")

    def is_winner_player(self, type):
        if self.list[DOWN_LEFT_CORNER] == type and self.list[DOWN] == type and self.list[DOWN_RIGHT_CORNER] == type:
            return True
        elif self.list[LEFT] == type and self.list[CENTER] == type and self.list[RIGHT] == type:
            return True
        if self.list[UP_LEFT_CORNER] == type and self.list[UP] == type and self.list[UP_RIGHT_CORNER] == type:
            return True
        if self.list[DOWN_LEFT_CORNER] == type and self.list[LEFT] == type and self.list[UP_LEFT_CORNER] == type:
            return True
        if self.list[DOWN] == type and self.list[CENTER] == type and self.list[UP] == type:
            return True
        if self.list[DOWN_RIGHT_CORNER] == type and self.list[RIGHT] == type and self.list[UP_RIGHT_CORNER] == type:
            return True
        if self.list[DOWN_RIGHT_CORNER] == type and self.list[CENTER] == type and self.list[UP_LEFT_CORNER] == type:
            return True
        if self.list[DOWN_LEFT_CORNER] == type and self.list[CENTER] == type and self.list[UP_RIGHT_CORNER] == type:
            return True

        return False

    def is_grid_full(self, run):
        if run == 9:
            self.get_snapschoot()
            print ("\n")
            print ("\033[31;1mResult:\033[0m Draw! ")
            print ("\n")
            return True
        else:
            return False

    def get_grid(self):
        return self.list

    def get_snapschoot(self):
        os.system("clear")
        self.print_grid()

