# Computer
# Authors Mario Carricato & Marco Amato

import random
from Utility import Common


class Computer:
    def __init__(self):
        self.type = "O"

    def get_move_ai(self, grid):
        for i in [Common.DOWN_LEFT_CORNER, Common.LEFT, Common.UP_LEFT_CORNER]:
            if grid[i + 1] == self.type and grid[i + 2] == self.type and grid[i] == str(i):
                return i
            elif grid[i] == self.type and grid[i + 2] == self.type and grid[i + 1] == str(i + 1):
                return i + 1
            elif grid[i] == self.type and grid[i + 1] == self.type and grid[i + 2] == str(i + 2):
                return i + 2
        for i in [Common.DOWN_LEFT_CORNER, Common.LEFT, Common.UP_LEFT_CORNER]:
            if grid[i + 1] == "X" and grid[i + 2] == "X" and grid[i] == str(i):
                return i
            elif grid[i] == "X" and grid[i + 2] == "X" and grid[i + 1] == str(i + 1):
                return i + 1
            elif grid[i] == "X" and grid[i + 1] == "X" and grid[i + 2] == str(i + 2):
                return i + 2

        for i in [Common.DOWN_LEFT_CORNER, Common.DOWN, Common.DOWN_RIGHT_CORNER]:
            if grid[i + 3] == self.type and grid[i + 6] == self.type and grid[i] == str(i):
                return i
            elif grid[i] == self.type and grid[i + 6] == self.type and grid[i + 3] == str(i + 3):
                return i + 3
            elif grid[i] == self.type and grid[i + 3] == self.type and grid[i + 6] == str(i + 6):
                return i + 6
        for i in [Common.DOWN_LEFT_CORNER, Common.DOWN, Common.DOWN_RIGHT_CORNER]:
            if grid[i + 3] == "X" and grid[i + 6] == "X" and grid[i] == str(i):
                return i
            elif grid[i] == "X" and grid[i + 6] == "X" and grid[i + 3] == str(i + 3):
                return i + 3
            elif grid[i] == "X" and grid[i + 3] == "X" and grid[i + 6] == str(i + 6):
                return i + 6

        if grid[Common.DOWN_LEFT_CORNER] == self.type and grid[Common.CENTER] == self.type and grid[
            Common.UP_RIGHT_CORNER] == str(9):
            return 9
        elif grid[Common.DOWN_LEFT_CORNER] == self.type and grid[Common.UP_RIGHT_CORNER] == self.type and grid[
            Common.CENTER] == str(5):
            return 5
        elif grid[Common.DOWN_LEFT_CORNER] == str(1) and grid[Common.CENTER] == self.type and grid[
            Common.UP_RIGHT_CORNER] == self.type:
            return 1
        if grid[Common.DOWN_LEFT_CORNER] == "X" and grid[Common.CENTER] == "X" and grid[Common.UP_RIGHT_CORNER] == str(9):
            return 9
        elif grid[Common.DOWN_LEFT_CORNER] == "X" and grid[Common.UP_RIGHT_CORNER] == "X" and grid[Common.CENTER] == str(5):
            return 5
        elif grid[Common.DOWN_LEFT_CORNER] == str(1) and grid[Common.CENTER] == "X" and grid[
            Common.UP_RIGHT_CORNER] == "X":
            return 1

        if grid[Common.DOWN_RIGHT_CORNER] == self.type and grid[Common.CENTER] == self.type and grid[
            Common.UP_LEFT_CORNER] == str(7):
            return 7
        elif grid[Common.DOWN_RIGHT_CORNER] == self.type and grid[Common.UP_LEFT_CORNER] == self.type and grid[
            Common.CENTER] == str(5):
            return 5
        elif grid[3] == str(Common.DOWN_RIGHT_CORNER) and grid[Common.CENTER] == self.type and grid[
            Common.UP_LEFT_CORNER] == self.type:
            return 3
        if grid[Common.DOWN_RIGHT_CORNER] == "X" and grid[Common.CENTER] == "X" and grid[Common.UP_LEFT_CORNER] == str(7):
            return 7
        elif grid[Common.DOWN_RIGHT_CORNER] == "X" and grid[Common.UP_LEFT_CORNER] == "X" and grid[Common.CENTER] == str(5):
            return 5
        elif grid[Common.DOWN_RIGHT_CORNER] == str(3) and grid[Common.CENTER] == "X" and grid[
            Common.UP_LEFT_CORNER] == "X":
            return 3

        if grid[Common.CENTER] == "5":
            return 5
        else:
            mv = random.randint(1, 9)
            return mv
