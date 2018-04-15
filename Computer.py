# Computer
# Authors Mario Carricato & Marco Amato

# positions
LEFT = 4
CENTER = 5
RIGHT = 6
UP = 8
DOWN = 2
UP_LEFT_CORNER = 7
UP_RIGHT_CORNER = 9
DOWN_LEFT_CORNER = 1
DOWN_RIGHT_CORNER = 3

import random


class Computer:
    def __init__(self):
        self.type = "O"

    def get_move_ai(self, grid):
        for i in [DOWN_LEFT_CORNER, LEFT, UP_LEFT_CORNER]:
            if grid[i + 1] == self.type and grid[i + 2] == self.type and grid[i] == str(i):
                return i
            elif grid[i] == self.type and grid[i + 2] == self.type and grid[i + 1] == str(i + 1):
                return i + 1
            elif grid[i] == self.type and grid[i + 1] == self.type and grid[i + 2] == str(i + 2):
                return i + 2
        for i in [DOWN_LEFT_CORNER, LEFT, UP_LEFT_CORNER]:
            if grid[i + 1] == "X" and grid[i + 2] == "X" and grid[i] == str(i):
                return i
            elif grid[i] == "X" and grid[i + 2] == "X" and grid[i + 1] == str(i + 1):
                return i + 1
            elif grid[i] == "X" and grid[i + 1] == "X" and grid[i + 2] == str(i + 2):
                return i + 2

        for i in [DOWN_LEFT_CORNER, DOWN, DOWN_RIGHT_CORNER]:
            if grid[i + 3] == self.type and grid[i + 6] == self.type and grid[i] == str(i):
                return i
            elif grid[i] == self.type and grid[i + 6] == self.type and grid[i + 3] == str(i + 3):
                return i + 3
            elif grid[i] == self.type and grid[i + 3] == self.type and grid[i + 6] == str(i + 6):
                return i + 6
        for i in [DOWN_LEFT_CORNER, DOWN, DOWN_RIGHT_CORNER]:
            if grid[i + 3] == "X" and grid[i + 6] == "X" and grid[i] == str(i):
                return i
            elif grid[i] == "X" and grid[i + 6] == "X" and grid[i + 3] == str(i + 3):
                return i + 3
            elif grid[i] == "X" and grid[i + 3] == "X" and grid[i + 6] == str(i + 6):
                return i + 6

        if grid[DOWN_LEFT_CORNER] == self.type and grid[CENTER] == self.type and grid[UP_RIGHT_CORNER] == str(9):
            return 9
        elif grid[DOWN_LEFT_CORNER] == self.type and grid[UP_RIGHT_CORNER] == self.type and grid[CENTER] == str(5):
            return 5
        elif grid[DOWN_LEFT_CORNER] == str(1) and grid[CENTER] == self.type and grid[UP_RIGHT_CORNER] == self.type:
            return 1
        if grid[DOWN_LEFT_CORNER] == "X" and grid[CENTER] == "X" and grid[UP_RIGHT_CORNER] == str(9):
            return 9
        elif grid[DOWN_LEFT_CORNER] == "X" and grid[UP_RIGHT_CORNER] == "X" and grid[CENTER] == str(5):
            return 5
        elif grid[DOWN_LEFT_CORNER] == str(1) and grid[CENTER] == "X" and grid[UP_RIGHT_CORNER] == "X":
            return 1

        if grid[DOWN_RIGHT_CORNER] == self.type and grid[CENTER] == self.type and grid[UP_LEFT_CORNER] == str(7):
            return 7
        elif grid[DOWN_RIGHT_CORNER] == self.type and grid[UP_LEFT_CORNER] == self.type and grid[CENTER] == str(5):
            return 5
        elif grid[3] == str(DOWN_RIGHT_CORNER) and grid[CENTER] == self.type and grid[UP_LEFT_CORNER] == self.type:
            return 3
        if grid[DOWN_RIGHT_CORNER] == "X" and grid[CENTER] == "X" and grid[UP_LEFT_CORNER] == str(7):
            return 7
        elif grid[DOWN_RIGHT_CORNER] == "X" and grid[UP_LEFT_CORNER] == "X" and grid[CENTER] == str(5):
            return 5
        elif grid[DOWN_RIGHT_CORNER] == str(3) and grid[CENTER] == "X" and grid[UP_LEFT_CORNER] == "X":
            return 3

        if grid[CENTER] == "5":
            return 5
        else:
            mv = random.randint(1, 9)
            return mv
