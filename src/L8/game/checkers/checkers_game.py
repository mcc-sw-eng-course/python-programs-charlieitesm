from abc import ABC
from L8.constants.constants import MOVE

from L8.board.board import Board
from L8.game.checkers.checkers_move import CheckersMove
from L8.game.checkers.checkers_utils import CheckerGameUtil
from L8.game.game import Game
from L8.player.player import Player


class CheckersGame(Game, ABC):

    def __init__(self, board: Board, players: list):
        super().__init__(board, players, True)

    def is_valid_move(self, move: dict, player: Player) -> bool:
        r1, c1, r2, c2 = move[MOVE]
        if player.game_token is "kw":
            player_color = "w"
        elif player.game_token is "kb":
            player_color = "b"
        else:
            player_color = player.game_token
        move = CheckersMove(r1, c1, r2, c2)
        return CheckerGameUtil.is_valid_move(move, player_color, self.board)

    def is_game_over(self) -> bool:
        return CheckerGameUtil.check_if_game_is_over(self.board)

    def finish_game(self):
        result = "draw"
        if len(CheckerGameUtil.get_valid_moves_for_player(self.board, self.board.w) is 0):
            result = "Black Player wins"
        elif len(CheckerGameUtil.get_valid_moves_for_player(self.board, self.board.b) is 0):
            result = "White Player wins"
        for p in self.players:
            p.ui.output(result)
