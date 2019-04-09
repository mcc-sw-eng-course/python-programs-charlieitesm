from abc import ABC
from L8.constants.constants import MOVE

from L8.board.board import Board
from L8.game.checkers.checkers_move import CheckersMove
from L8.game.checkers.checkers_utils import CheckerGameUtil
from L8.game.game import Game
from L8.player.player import Player


class CheckersGame(Game, ABC):

    def __init__(self, board: Board, players: list):
        super().__init__(board, players)

    def is_valid_move(self, move: dict, player: Player) -> bool:
        r1, c1, r2, c2, is_jump, player_color = move[MOVE]
        move = CheckersMove(r1, c1, r2, c2, is_jump)
        return CheckerGameUtil.is_valid_move(move, player_color, self.board)

    def is_game_over(self) -> bool:
        pass

    def finish_game(self):
        pass
