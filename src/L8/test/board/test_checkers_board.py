from unittest import TestCase

from L8.board.checkers_board import CheckersBoard
from L8.game.game_token import CHECKERS_TOKENS


class TestTicTacToeBoard(TestCase):

    def setUp(self):
        self.under_test = CheckersBoard()

        for t in CHECKERS_TOKENS:
            if str(t) == "W":
                self.w = t
            elif str(t) == "B":
                self.b = t
            elif str(t) == "KB":
                self.kb = t
            elif str(t) == "KW":
                self.kw = t

    def test_init_board(self):
        self.assertIsNotNone(self.under_test)
        self.assertIsNotNone(self.under_test.current_state)
        self.assertEqual(8, len(self.under_test.current_state))

        for row in self.under_test.current_state:
            self.assertEqual(8, len(row))

    def test_correct_initial_board(self):
        expected_board = [
            [None, self.w, None, self.w, None, self.w, None, self.w],
            [self.w, None, self.w, None, self.w, None, self.w, None],
            [None, self.w, None, self.w, None, self.w, None, self.w],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [self.b, None, self.b, None, self.b, None, self.b, None],
            [None, self.b, None, self.b, None, self.b, None, self.b],
            [self.b, None, self.b, None, self.b, None, self.b, None]
        ]

        for i, row in enumerate(self.under_test.current_state):
            for j, cell in enumerate(row):
                expected_token = expected_board[i][j]
                self.assertEqual(expected_token, cell)

    def test_str_representation(self):

        expected_board = [
            [None, self.w, None, self.w, None, self.w, None, self.w],
            [self.w, None, self.w, None, self.w, None, self.w, None],
            [None, self.w, None, self.w, None, self.w, None, self.w],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [self.b, None, self.b, None, self.b, None, self.b, None],
            [None, self.b, None, self.b, None, self.b, None, self.b],
            [self.b, None, self.b, None, self.b, None, self.b, None]
        ]

        self.under_test.current_state = expected_board

        expected_str_representation = "\n".join(
            [
                "   | W |   | W |   | W |   | W ",
                " W |   | W |   | W |   | W |   ",
                "   | W |   | W |   | W |   | W ",
                "   |   |   |   |   |   |   |   ",
                "   |   |   |   |   |   |   |   ",
                " B |   | B |   | B |   | B |   ",
                "   | B |   | B |   | B |   | B ",
                " B |   | B |   | B |   | B |   "
             ])
        self.assertEqual(expected_str_representation, str(self.under_test))

    def test_serialize(self):

        expected_board = [
            [None, self.w, None, self.w, None, self.w, None, self.w],
            [self.w, None, self.w, None, self.w, None, self.w, None],
            [None, self.w, None, self.w, None, self.w, None, self.w],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [self.b, None, self.b, None, self.b, None, self.b, None],
            [None, self.b, None, self.b, None, self.b, None, self.b],
            [self.b, None, self.b, None, self.b, None, self.b, None]
        ]

        self.under_test.current_state = expected_board

        expected_str = ",W,,W,,W,,W,W,,W,,W,,W,,,W,,W,,W,,W,,,,,,,,,,,,,,,,,B,,B,,B,,B,,,B,,B,,B,,B,B,,B,,B,,B,"

        self.assertEqual(expected_str, self.under_test.serialize())

    def test_deserialize(self):

        expected_board = [
            [None, self.w, None, self.w, None, self.w, None, self.w],
            [self.w, None, self.w, None, self.w, None, self.w, None],
            [None, None, None, self.w, None, self.w, None, self.w],
            [self.kw, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, self.kb],
            [self.b, None, self.b, None, self.b, None, None, None],
            [None, self.b, None, self.b, None, self.b, None, self.b],
            [self.b, None, self.b, None, self.b, None, self.b, None]
        ]

        serialized_str = "".join([
            ",W,,W,,W,,W,",
            "W,,W,,W,,W,,",
            ",,,W,,W,,W,",
            "KW,,,,,,,,",
            ",,,,,,,KB,",
            "B,,B,,B,,,,",
            ",B,,B,,B,,B,",
            "B,,B,,B,,B,"
        ])

        self.under_test.deserialize(serialized_str)

        for i, row in enumerate(self.under_test.current_state):
            for j, cell in enumerate(row):
                self.assertEqual(expected_board[i][j], cell)
