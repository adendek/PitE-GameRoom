1#Grid
#Authors Mario Carricato & Marco Amato

import os
import Common

class Grid:
    def __init__(self):
        self.list = ["", str(Common.DOWN_LEFT_CORNER), str(Common.DOWN), str(Common.DOWN_RIGHT_CORNER), str(Common.LEFT), str(Common.CENTER), str(Common.RIGHT), str(Common.UP_LEFT_CORNER), str(Common.UP), str(Common.UP_RIGHT_CORNER)]

    def print_grid(self):
        print ("   |   |   ")
        print (" " + self.list[int(Common.UP_LEFT_CORNER)] + " | " + self.list[int(Common.UP)] + " | " + self.list[int(Common.UP_RIGHT_CORNER)] + "  ")
        print ("   |   |   ")
        print ("-----------")
        print ("   |   |   ")
        print (" " + self.list[int(Common.LEFT)] + " | " + self.list[int(Common.CENTER)] + " | " + self.list[int(Common.RIGHT)] + "  ")
        print ("   |   |   ")
        print ("-----------")
        print ("   |   |   ")
        print (" " + self.list[int(Common.DOWN_LEFT_CORNER)] + " | " + self.list[int(Common.DOWN)] + " | " + self.list[int(Common.DOWN_RIGHT_CORNER)] + "  ")
        print ("   |   |   ")

    def draw_grid(self, list):
        if(len(list))>0:
            print ("   |   |   ")
            print (" " + list[int(Common.UP_LEFT_CORNER)] + " | " + list[int(Common.UP)] + " | " + list[int(Common.UP_RIGHT_CORNER)] + "  ")
            print ("   |   |   ")
            print ("-----------")
            print ("   |   |   ")
            print (" " + list[int(Common.LEFT)] + " | " + list[int(Common.CENTER)] + " | " + list[int(Common.RIGHT)] + "  ")
            print ("   |   |   ")
            print ("-----------")
            print ("   |   |   ")
            print (" " + list[int(Common.DOWN_LEFT_CORNER)] + " | " + list[int(Common.DOWN)] + " | " + list[int(Common.DOWN_RIGHT_CORNER)] + "  ")
            print ("   |   |   ")

            return True
        else:
            return False

    def is_winner_player(self, type):
        if self.list[int(Common.DOWN_LEFT_CORNER)] == type and self.list[int(Common.DOWN)] == type and self.list[int(Common.DOWN_RIGHT_CORNER)] == type:
            return True
        elif self.list[int(Common.LEFT)] == type and self.list[int(Common.CENTER)] == type and self.list[int(Common.RIGHT)] == type:
            return True
        if self.list[int(Common.UP_LEFT_CORNER)] == type and self.list[int(Common.UP)] == type and self.list[int(Common.UP_RIGHT_CORNER)] == type:
            return True
        if self.list[int(Common.DOWN_LEFT_CORNER)] == type and self.list[int(Common.LEFT)] == type and self.list[int(Common.UP_LEFT_CORNER)] == type:
            return True
        if self.list[int(Common.DOWN)] == type and self.list[int(Common.CENTER)] == type and self.list[int(Common.UP)] == type:
            return True
        if self.list[int(Common.DOWN_RIGHT_CORNER)] == type and self.list[int(Common.RIGHT)] == type and self.list[int(Common.UP_RIGHT_CORNER)] == type:
            return True
        if self.list[int(Common.DOWN_RIGHT_CORNER)] == type and self.list[int(Common.CENTER)] == type and self.list[int(Common.UP_LEFT_CORNER)] == type:
            return True
        if self.list[int(Common.DOWN_LEFT_CORNER)] == type and self.list[int(Common.CENTER)] == type and self.list[int(Common.UP_RIGHT_CORNER)] == type:
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

