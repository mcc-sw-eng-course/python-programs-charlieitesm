from enum import Enum


class GameMode(Enum):
    LOCAL = "local"
    CLIENT = "client"
    SERVER = "server"


class TypeOfUI(Enum):
    CONSOLE = "console"


class GameName(Enum):
    TIC_TAC_TOE = "tic_tac_toe"


class GameLevel(Enum):
    EASY = "easy"
    NORMAL = "normal"
    HARD = "hard"


GAME_TOKEN = "game_token"
MOVE = "move"
