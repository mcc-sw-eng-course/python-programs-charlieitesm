from abc import ABC

from L8.board.board import Board
from L8.board.tic_tac_toe_board import TicTacToeBoard
from L8.constants.constants import MOVE
from L8.game.game import Game
from L8.game.game_token import GameToken
from L8.game.local_game import LocalGame
from L8.messages.english import TICTACTOE_ENDING_MESSAGE, TICTACTOE_DRAW_MESSAGE, WINNER_MESSAGE
from L8.player.player import Player


class TicTacToeGame(Game, ABC):

    LEGAL_TOKENS = [GameToken("X"), GameToken("O")]

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
        winner_result = TICTACTOE_DRAW_MESSAGE if not self.winner else f"{WINNER_MESSAGE} {self.winner}"
        final_message = "\n".join([TICTACTOE_ENDING_MESSAGE, str(self.board), winner_result])

        for p in self.players:
            p.ui.output(final_message)


class TicTacToeLocalGame(TicTacToeGame, LocalGame):
    def __init__(self, players: list):
        super().__init__(players)


class TicTacToeGameUtil:

    @staticmethod
    def is_legal_tic_tac_toe_move(board: Board, move_x: int, move_y: int) -> bool:
        """
        Determines if the move made by player is legal on this board

        In general, a Tic Tac Toe is valid if:
        1. It is made within the bounds of the board
        2. The space that is intended to be used is not already in use
        :param board: a Board where you want to check the move
        :param move_x: an int with the x coordinate for the move
        :param move_y: an int with the y coordinate for the move
        :return: True if the move is valid, False otherwise.
        """
        board_size = len(board.current_state)

        # Check if the move is within bounds
        if not 0 <= move_x < board_size or not 0 <= move_y < board_size:
            return False

        # Check the space is not in use already
        value_at_board = board.current_state[move_x][move_y]

        if value_at_board is not None:
            return False

        return True

    @staticmethod
    def get_winner(board: Board) -> GameToken:
        for x, row in enumerate(board.current_state):
            for y, gt in enumerate(row):

                # There will be no winner combination on this row/column
                if gt is None:
                    continue

                if TicTacToeGameUtil.check_complete_line_in_board(board, gt, x, y):
                    winner_token = gt
                    return winner_token

    @staticmethod
    def check_complete_line_in_board(board: Board, game_token: GameToken, x: int, y: int) -> bool:
        """
        Checks if there are exactly three tokens equal to val horizontally, vertically and diagonally on the board
        respective to x and y
        :param board: the Board in which to check the line
        :param game_token: a str representing the game_token to look for
        :param x: an int representing the original X coordinate of val
        :param y: an int representing the original Y coordinate of val
        :return: True if a line of successive val was found, False if otherwise
        """
        num_of_same_tokens = 0
        len_of_board = len(board.current_state)

        # Check horizontally
        for j in range(len_of_board):
            if board.current_state[x][j] == game_token:
                num_of_same_tokens += 1
            else:
                break

        if num_of_same_tokens == 3:
            return True

        num_of_same_tokens = 0

        # Check vertically
        for i in range(len_of_board):
            if board.current_state[i][y] == game_token:
                num_of_same_tokens += 1
            else:
                break

        if num_of_same_tokens == 3:
            return True

        num_of_same_tokens = 0

        # Check diagonally top to bottom, but only if we can do so
        if (x, y) in ((0, 0), (1, 1), (2, 2), (2, 0), (0, 2)):

            # Left to right:
            for i in range(len_of_board):
                if game_token != board.current_state[i][i]:
                    break
                else:
                    num_of_same_tokens += 1

            if num_of_same_tokens == 3:
                return True

            num_of_same_tokens = 0

            # Right to left
            for k in range(len_of_board):
                i = 0 + k
                j = 2 - k
                if game_token == board.current_state[i][j]:
                    num_of_same_tokens += 1

            return num_of_same_tokens == 3

        else:
            return False

