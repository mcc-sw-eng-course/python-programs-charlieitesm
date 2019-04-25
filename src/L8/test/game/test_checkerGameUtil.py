from unittest import TestCase

from L8.board.checkers_board import CheckersBoard
from L8.game.checkers.checkers_move import CheckersMove
from L8.game.checkers.checkers_utils import CheckerGameUtil
from L8.game.game_token import CHECKERS_TOKENS


class TestCheckerGameUtil(TestCase):
    def setUp(self) -> None:
        self.w = [t for t in CHECKERS_TOKENS if str(t) == "W"][0]
        self.b = [t for t in CHECKERS_TOKENS if str(t) == "B"][0]
        self.kw = [t for t in CHECKERS_TOKENS if str(t) == "KW"][0]
        self.kb = [t for t in CHECKERS_TOKENS if str(t) == "KB"][0]

    def test_can_jump(self):
        test_board = [
            [None, self.w, None, self.w, None, self.w, None, self.w],
            [self.w, None, self.w, None, self.w, None, self.w, None],
            [None, self.w, None, None, None, self.w, None, self.w],
            [None, None, None, None, None, self.w, None, None],
            [None, None, None, None, None, None, self.b, None],
            [self.b, None, self.b, None, self.b, None, None, None],
            [None, self.b, None, self.b, None, self.b, None, self.b],
            [self.b, None, self.b, None, self.b, None, self.b, None]
        ]

        board = CheckersBoard()
        board.current_state = test_board

        # Let's try to see if the W piece at 3,5 can jump (it should)
        r1 = 3
        c1 = 5
        r2 = r1 + 1
        c2 = c1 + 1
        destination_row = r1 + 2
        destination_column = c1 + 2

        self.assertEqual(test_board[r1][c1], self.w)
        self.assertEqual(test_board[r2][c2], self.b)
        self.assertIsNone(test_board[destination_row][destination_column])

        self.assertTrue(
            CheckerGameUtil.can_jump(self.w, r1, c1, r2, c2, destination_row, destination_column, board))
        self.assertTrue(CheckerGameUtil.can_jump(self.b, r2, c2, r1, c1, r2 - 2, c2 - 2, board))
        self.assertFalse(CheckerGameUtil.can_jump(self.w, r1, c1, r1 - 1, c1 - 1, r1 - 2, c2 - 2, board))

    def test_get_valid_moves_for_player(self):
        test_board = [
            [None, self.w, None, self.w, None, self.w, None, self.w],
            [self.w, None, self.w, None, self.w, None, self.w, None],
            [None, self.w, None, None, None, self.w, None, self.w],
            [None, None, None, None, None, self.w, None, None],
            [None, None, None, None, None, None, self.b, None],
            [self.b, None, self.b, None, self.b, None, None, None],
            [None, self.b, None, self.b, None, self.b, None, self.b],
            [self.b, None, self.b, None, self.b, None, self.b, None]
        ]

        board = CheckersBoard()
        board.current_state = test_board

        origin_row = 3
        origin_column = 5
        destination_row = origin_row + 2
        destination_column = origin_column + 2

        # The only possible move for W should be to jump once
        result = CheckerGameUtil.get_valid_moves_for_player(board, self.w)

        self.assertTrue(len(result) == 1)

        jump_move = result[0]

        self.assertEqual(origin_row, jump_move.fr)
        self.assertEqual(origin_column, jump_move.fc)
        self.assertEqual(destination_row, jump_move.tr)
        self.assertEqual(destination_column, jump_move.tc)

    def test_is_game_over(self):
        test_board = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, self.b, None],
            [self.b, None, self.b, None, self.b, None, None, None],
            [None, self.b, None, self.b, None, self.b, None, self.b],
            [self.b, None, self.b, None, self.b, None, self.b, None]
        ]
        board = CheckersBoard()
        board.current_state = test_board
        self.assertTrue(CheckerGameUtil.check_if_game_is_over(board))
        test_board = [
            [None, None, self.w, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, self.b, None],
            [self.b, None, self.b, None, self.b, None, None, None],
            [None, self.b, None, self.b, None, self.b, None, self.b],
            [self.b, None, self.b, None, self.b, None, self.b, None]
        ]
        board = CheckersBoard()
        board.current_state = test_board
        self.assertFalse(CheckerGameUtil.check_if_game_is_over(board))

    def test_get_valid_moves_for_player(self):
        test_board = [
            [None, None, None, None, None, None, None, None],
            [None, self.b, None, self.b, None, None, None, None],
            [None, None, self.kw, None, None, None, None, None],
            [None, self.b, None, self.b, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None]
        ]
        board = CheckersBoard()
        board.current_state = test_board
        move = CheckersMove(2, 2, 0, 0)
        self.assertTrue(len(CheckerGameUtil.get_valid_moves_for_player(board, self.w)) is 4)
        self.assertTrue(CheckerGameUtil.is_valid_move(move, self.w, board))
        self.assertTrue(len(CheckerGameUtil.get_jumps_from_position(self.w, 2, 2, board)))

        test_board = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, self.kw, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, self.kw, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None]
        ]
        board = CheckersBoard()
        board.current_state = test_board
        self.assertTrue(len(CheckerGameUtil.get_valid_moves_for_player(board, self.w)) is 8)
        self.assertFalse(CheckerGameUtil.is_valid_move(move, self.w, board))
