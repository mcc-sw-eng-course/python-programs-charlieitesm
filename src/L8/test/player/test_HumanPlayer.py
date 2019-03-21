from unittest import TestCase

from L8.board.tic_tac_toe_board import TicTacToeBoard
from L8.constants.constants import MOVE, GAME_TOKEN
from L8.game.game_token import GameToken
from L8.player.human_player import HumanPlayer
from L8.ui.ui import DummyUI


class TestHumanPlayer(TestCase):

    def setUp(self):
        HumanPlayer.PLAYER_NUM = 1

        self.ui = DummyUI()
        self.game_token = GameToken("X")
        self.under_test = HumanPlayer(self.ui, self.game_token)

    def tearDown(self):
        HumanPlayer.PLAYER_NUM = 1

    def test_generate_name(self):
        expected = "H_P1"
        self.assertEqual(expected, self.under_test.name)

        expected = "H_P2"
        self.under_test = HumanPlayer(self.ui, self.game_token)
        self.assertEqual(expected, self.under_test.name)

        expected = "H_P3"
        self.under_test = HumanPlayer(self.ui, self.game_token)
        self.assertEqual(expected, self.under_test.name)

    def test_make_move(self):
        # Mock the input
        self.ui.input = lambda msg: "0,1"
        expected = (0, 1)

        result = self.under_test.make_move(TicTacToeBoard())
        self.assertIsNotNone(result)
        self.assertTrue(MOVE in result)
        self.assertTrue(GAME_TOKEN in result)
        self.assertEqual(self.game_token, result[GAME_TOKEN])
        self.assertEqual(expected, result[MOVE])
