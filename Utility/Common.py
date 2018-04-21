import enum

LEFT = 4
CENTER = 5
RIGHT = 6
UP = 8
DOWN = 2
UP_LEFT_CORNER = 7
UP_RIGHT_CORNER = 9
DOWN_LEFT_CORNER = 1
DOWN_RIGHT_CORNER = 3


class GamesType(enum.Enum):
    TicTacToe = 1
    GuessNumber = 2


class PlayerType(enum.Enum):
    Player1 = 0
    Player2 = 1


class MessageType(enum.Enum):
    UPDATE_GUI = 0
    MOVE_REQUEST = 1
    END_GAME = 2
    CHECK_ATTEMPTS = 32
    RESPONSE = 4


class ServerState(enum.Enum):
    LISTEN = 1
    CONNECTED = 2
    REFRESH = 3


class ServerEvent(enum.Enum):
    WAIT_PLAYER = 1
    START_MATCH = 2
    FINISH_MATCH = 3
    END_REINIT = 4