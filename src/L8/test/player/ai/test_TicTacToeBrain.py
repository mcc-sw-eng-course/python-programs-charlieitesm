from unittest import TestCase

from L8.board.tic_tac_toe_board import TicTacToeBoard
from L8.constants.constants import GameLevel
from L8.game.tic_tac_toe_game import TicTacToeGame
from L8.player.ai.tic_tac_toe_brain import TicTacToeBrain


class TestTicTacToeBrain(TestCase):

    def setUp(self):
        legal_tokens = TicTacToeGame.LEGAL_TOKENS

        for t in legal_tokens:
            if str(t) == "X":
                self.x_token = t
            elif str(t) == "O":
                self.o_token = t

    def test_easy_mode(self):
        test_board = [
            [self.x_token, None, None],
            [self.o_token, None, None],
            [None, None, None],
        ]
        board = TicTacToeBoard()
        board.current_state = test_board

        under_test = TicTacToeBrain(GameLevel.EASY)
        result = under_test.calculate_next_move(board, self.o_token)

        self.assertIsNotNone(result)

    def test_normal_mode(self):
        test_board = [
            [self.x_token, None, None],
            [self.o_token, None, None],
            [None, None, None],
        ]
        board = TicTacToeBoard()
        board.current_state = test_board

        under_test = TicTacToeBrain(GameLevel.NORMAL)
        result = under_test.calculate_next_move(board, self.o_token)

        self.assertIsNotNone(result)

    def test_hard_mode(self):
        test_board = [
            [self.x_token, None, None],
            [self.o_token, None, None],
            [None, None, None],
        ]
        board = TicTacToeBoard()
        board.current_state = test_board

        under_test = TicTacToeBrain(GameLevel.HARD)
        result = under_test.calculate_next_move(board, self.o_token)

        self.assertIsNotNone(result)

