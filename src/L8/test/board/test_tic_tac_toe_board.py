from unittest import TestCase

from L8.board.tic_tac_toe_board import TicTacToeBoard


class TestTicTacToeBoard(TestCase):

    def setUp(self):
        self.under_test = TicTacToeBoard()

    def test_init_board(self):
        self.assertIsNotNone(self.under_test)
        self.assertIsNotNone(self.under_test.current_state)

        for row in self.under_test.current_state:
            self.assertTrue(len(row) == 3)

    def test_str_representation(self):
        # Let's inject a board that show a game in progress
        simulated_board = [
            ["X", "O", None],
            ["X", "X", None],
            [None, None, "O"]
        ]

        self.under_test.current_state = simulated_board

        expected_str_board = " X | O |   \n X | X |   \n   |   | O "
        str_board = str(self.under_test)
        self.assertEqual(expected_str_board, str_board, "The board was not printed as expected")
