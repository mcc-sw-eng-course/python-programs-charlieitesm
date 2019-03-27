from abc import ABC

from L8.board.tic_tac_toe_board import TicTacToeBoard
from L8.constants.constants import MOVE
from L8.game.client_game import ClientGame
from L8.game.game import Game
from L8.game.local_game import LocalGame
from L8.game.server_game import ServerGame
from L8.game.tic_tac_toe.util import TicTacToeGameUtil
from L8.messages.english import TICTACTOE_ENDING_MSG, TICTACTOE_DRAW_MSG, WINNER_MSG, YOU_WIN_MSG, YOU_LOSE_MSG
from L8.player.player import Player


class TicTacToeGame(Game, ABC):

    def __init__(self, players: list):
        super().__init__(TicTacToeBoard(), players)

    def set_up_game(self):
        pass

    def is_valid_move(self, move: dict, player: Player) -> bool:
        """
        Determines if the move made by player is legal on this board

        In general, a Tic Tac Toe is valid if:
        1. It is made within the bounds of the board
        2. The space that is intended to be used is not already in use

        :param move: a dict with the move and the game_token to be placed by player
        :param player: a Player making the move. For TicTacToe, the player is not relevant
        :return: True if the move is valid, False otherwise.
        """

        move_x, move_y = move[MOVE]

        return TicTacToeGameUtil.is_legal_tic_tac_toe_move(self.board, move_x, move_y)

    def is_game_over(self) -> bool:
        """
        Determines if the game is already over

        In general, a TicTacToe game is over if:
        1. There is a line of the same game_token horizontally, vertically or diagonally
        2. There are no more spaces to use
        :return:
        """
        # Check if we have a winner
        winning_token = TicTacToeGameUtil.get_winner(self.board)

        if winning_token:
            self.winner = self.token_to_player(winning_token)
            return True

        # Check if there are no more places to put a game_token
        for row in self.board.current_state:
            for val in row:
                if val is None:
                    return False
        return True

    def finish_game(self):
        """
        Prepares and outputs to each of the players a message with the results
        :return:
        """
        winner_result = TICTACTOE_DRAW_MSG if not self.winner else f"{WINNER_MSG} {self.winner}"
        final_message = "\n".join([TICTACTOE_ENDING_MSG, str(self.board), winner_result])

        for p in self.players:
            p.ui.output(final_message)


class TicTacToeLocalGame(TicTacToeGame, LocalGame):
    def __init__(self, players: list):
        super().__init__(players)


class TicTacToeServerGame(TicTacToeGame, ServerGame):
    def __init__(self, players: list, port: int):
        super().__init__(players)
        self.port = port

    # Override the method so that the clients are not notified and are responsible for determining the final messages
    #  instead
    def finish_game(self):
        winner_result = TICTACTOE_DRAW_MSG if not self.winner else f"{WINNER_MSG} {self.winner}"
        final_message = "\n".join([TICTACTOE_ENDING_MSG, str(self.board), winner_result])
        self.LOGGER.info(final_message)


class TicTacToeClientGame(TicTacToeGame, ClientGame):
    def __init__(self, players: list, ip_address: str, port: int):
        super().__init__(players)
        self.ip_address = ip_address
        self.port = port

    def finish_game(self):
        winner_token = TicTacToeGameUtil.get_winner(self.board)
        client_player = self.players[0]

        if not winner_token:
            result_msg = TICTACTOE_DRAW_MSG
        elif winner_token == client_player.game_token:
            result_msg = YOU_WIN_MSG
        else:
            result_msg = YOU_LOSE_MSG

        final_message = "\n".join([TICTACTOE_ENDING_MSG, str(self.board), result_msg])
        client_player.ui.output(final_message)
