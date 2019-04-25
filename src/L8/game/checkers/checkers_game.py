from abc import ABC

from L8.board.checkers_board import CheckersBoard
from L8.constants.constants import MOVE, GAME_TOKEN
from L8.game.checkers.checkers_move import CheckersMove
from L8.game.checkers.checkers_utils import CheckerGameUtil
from L8.game.client_game import ClientGame
from L8.game.game import Game
from L8.game.local_game import LocalGame
from L8.game.server_game import ServerGame
from L8.player.player import Player


class CheckersGame(Game, ABC):

    def __init__(self, players: list):
        super().__init__(CheckersBoard(), players, True)

    def set_up_game(self):
        pass

    def make_move(self, move: dict, player: Player) -> bool:
        origin_x, origin_y, move_x, move_y = move[MOVE]
        legal_moves = CheckerGameUtil.get_valid_moves_for_player(self.board, player.game_token)
        checkers_move = CheckersMove(origin_x, origin_y, move_x, move_y)
        i = legal_moves.index(checkers_move)
        checkers_move = legal_moves[i]
        self.board.current_state[checkers_move.fr][checkers_move.fc] = None
        self.board.current_state[checkers_move.tr][checkers_move.tc] = move[GAME_TOKEN]
        if checkers_move.is_jump:
            self.board.current_state[checkers_move.jumped_enemy_row][checkers_move.jumped_enemy_col] = None
        return len(CheckerGameUtil.get_jumps_from_position(player.game_token, move_x, move_y, self.board)) > 0


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


class CheckersLocalGame(CheckersGame, LocalGame):
    def __init__(self, players: list):
        super().__init__(players)


class CheckersServerGame(CheckersGame, ServerGame):
    def __init__(self, players: list, port: int):
        super().__init__(players)
        self.port = port

    # Override the method so that the clients are not notified and are responsible for determining the final messages
    #  instead
    def finish_game(self):
        raise NotImplementedError


class CheckersClientGame(CheckersGame, ClientGame):
    def __init__(self, players: list, ip_address: str, port: int):
        super().__init__(players)
        self.ip_address = ip_address
        self.port = port

    def finish_game(self):
        raise NotImplementedError
