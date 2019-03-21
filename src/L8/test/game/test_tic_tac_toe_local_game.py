from unittest import TestCase

from L8.constants.constants import MOVE, GAME_TOKEN
from L8.game.tic_tac_toe_game import TicTacToeLocalGame, TicTacToeGameUtil
from L8.player.human_player import HumanPlayer
from L8.ui.ui import DummyUI


class TestTicTacToeLocalGame(TestCase):

    def setUp(self):
        self.x_token = [t for t in TicTacToeLocalGame.LEGAL_TOKENS if t.token_symbol == "X"][0]
        self.o_token = [t for t in TicTacToeLocalGame.LEGAL_TOKENS if t.token_symbol == "O"][0]

        # The player doesn't matter for TicTacToe, let's create a dummy one
        self.x_player = HumanPlayer(DummyUI(), self.x_token)
        self.o_player = HumanPlayer(DummyUI(), self.x_token)

        self.under_test = TicTacToeLocalGame([self.x_player, self.o_player])

    def test_set_up_game(self):
        self.under_test.set_up_game()

    def test_is_valid_move(self):
        x = self.x_token
        o = self.o_token

        test_board = [
            [x, None, o],
            [x, None, None],
            [o, None, x]
        ]

        self.under_test.board.current_state = test_board

        move = {
            MOVE: (0, 1),
            GAME_TOKEN: self.x_token
        }
        self.assertTrue(self.under_test.is_valid_move(move, self.x_player))

        move = {
            MOVE: (0, 0),
            GAME_TOKEN: self.x_token
        }
        self.assertFalse(self.under_test.is_valid_move(move, self.x_player))

        move = {
            MOVE: (-1, 0),
            GAME_TOKEN: self.x_token
        }
        self.assertFalse(self.under_test.is_valid_move(move, self.x_player))

        move = {
            MOVE: (4, 4),
            GAME_TOKEN: self.x_token
        }
        self.assertFalse(self.under_test.is_valid_move(move, self.x_player))

    def test_is_game_over(self):
        x = self.x_token
        o = self.o_token

        test_board = [
            [x, None, o],
            [x, None, None],
            [o, None, x]
        ]

        self.under_test.board.current_state = test_board
        self.assertFalse(self.under_test.is_game_over())

        test_board = [
            [x, None, o],
            [x, x, None],
            [o, None, x]
        ]

        self.under_test.board.current_state = test_board
        self.assertTrue(self.under_test.is_game_over())
        # X wins
        self.assertIsNotNone(self.under_test.winner)
        self.assertEqual(self.x_token, self.under_test.winner.game_token)

        self.under_test = TicTacToeLocalGame([self.x_player, self.o_player])

        test_board = [
            [x, x, o],
            [o, o, x],
            [x, o, x]
        ]

        self.under_test.board.current_state = test_board
        self.assertTrue(self.under_test.is_game_over())
        # It's a tie!
        self.assertIsNone(self.under_test.winner)

    def test_finish_game(self):
        x = self.x_token
        o = self.o_token

        test_board = [
            [x, None, o],
            [x, x, None],
            [o, None, x]
        ]
        self.under_test.board.current_state = test_board
        self.assertTrue(self.under_test.is_game_over())
        self.assertIsNotNone(self.under_test.winner)
        self.assertEqual(self.x_token, self.under_test.winner.game_token)
        self.under_test.finish_game()

    def test_check_complete_line_in_board(self):
        x = self.x_token
        o = self.o_token

        test_board = [
            [o, o, o],
            [x, x, None],
            [o, None, x]
        ]
        self.under_test.board.current_state = test_board
        # Horizontal
        self.assertTrue(TicTacToeGameUtil.check_complete_line_in_board(self.under_test.board, o, 0, 0))

        test_board = [
            [o, x, o],
            [x, x, None],
            [o, x, x]
        ]
        self.under_test.board.current_state = test_board
        # Vertical
        self.assertTrue(TicTacToeGameUtil.check_complete_line_in_board(self.under_test.board, x, 0, 1))

        test_board = [
            [x, o, o],
            [x, x, None],
            [o, None, x]
        ]
        self.under_test.board.current_state = test_board
        # Diagonal
        self.assertTrue(TicTacToeGameUtil.check_complete_line_in_board(self.under_test.board, x, 2, 2))

    def test_local_methods(self):
        # These methods shouldn't do anything
        self.under_test.initialize_resources()
        self.under_test.release_resources()
