import random

from L8.board.board import Board
from L8.constants.constants import GameLevel
from L8.game.checkers.checkers_utils import CheckerGameUtil
from L8.game.game_token import GameToken
from L8.player.ai.brain import Brain


class CheckersBrain(Brain):

    def __init__(self, level: GameLevel):
        super().__init__(level)

    def easy_mode(self, board: Board, game_token: GameToken) -> tuple:
        possible_moves = CheckerGameUtil.get_valid_moves_for_player(board, game_token.token_symbol)
        move = random.choice(possible_moves)
        return move.r1, move.c1, move.r2, move.c2

    def normal_mode(self, board: Board, game_token: GameToken) -> tuple:
        return self.easy_mode(board, game_token)

    def hard_mode(self, board: Board, game_token: GameToken) -> tuple:
        return self.easy_mode(board, game_token)
