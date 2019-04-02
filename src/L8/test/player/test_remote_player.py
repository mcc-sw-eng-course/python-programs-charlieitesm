from unittest import TestCase

from L8.board.tic_tac_toe_board import TicTacToeBoard
from L8.constants.constants import MOVE, GAME_TOKEN
from L8.game.game_token import GameToken
from L8.player.remote_player import RemotePlayer
from L8.ui.ui import DummyUI


class TestRemotePlayer(TestCase):

    def setUp(self):
        self.game_token = GameToken("X")
        self.under_test = RemotePlayer(self.game_token)
        self.under_test.ui = DummyUI()

    def test_generate_name(self):
        expected = "Remote_P1"
        self.assertEqual(expected, self.under_test.name)

        expected = "Remote_P2"
        remote_2 = RemotePlayer(self.game_token)
        self.assertEqual(expected, remote_2.name)

    def test_make_move(self):
        self.under_test.ui.input = lambda msg: "0,1"
        expected = (0, 1)
        result = self.under_test.make_move(TicTacToeBoard())
        self.assertIsNotNone(result)
        self.assertTrue(MOVE in result)
        self.assertTrue(GAME_TOKEN in result)
        self.assertEqual(self.game_token, result[GAME_TOKEN])
        self.assertEqual(expected, result[MOVE])


