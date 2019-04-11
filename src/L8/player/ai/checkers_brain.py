from L8.board.board import Board
from L8.constants.constants import GameLevel
from L8.game.game_token import GameToken
from L8.player.ai.brain import Brain


class CheckersBrain(Brain):

    def __init__(self, level: GameLevel):
        super().__init__(level)

    def easy_mode(self, board: Board, game_token: GameToken) -> tuple:
        raise NotImplementedError

    def normal_mode(self, board: Board, game_token: GameToken) -> tuple:
        raise NotImplementedError

    def hard_mode(self, board: Board, game_token: GameToken) -> tuple:
        raise NotImplementedError
