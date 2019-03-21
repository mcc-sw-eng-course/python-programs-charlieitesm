from unittest import TestCase

from L8.board.tic_tac_toe_board import TicTacToeBoard
from L8.constants.constants import GameLevel, MOVE, GAME_TOKEN
from L8.game.game_token import GameToken
from L8.player.ai.tic_tac_toe_brain import TicTacToeBrain
from L8.player.ai_player import AIPlayer


class TestAIPlayer(TestCase):

    def setUp(self):
        AIPlayer.PLAYER_NUM = 1
        self.game_token = GameToken("X")
        self.brain = TicTacToeBrain(GameLevel.EASY)
        self.under_test = AIPlayer(self.brain, self.game_token)

    def tearDown(self):
        AIPlayer.PLAYER_NUM = 1

    def test_generate_name(self):
        expected = "AI_1"
        self.assertEqual(expected, self.under_test.name)

        expected = "AI_2"
        self.brain = TicTacToeBrain(GameLevel.HARD)
        self.under_test = AIPlayer(self.brain, self.game_token)
        self.assertEqual(expected, self.under_test.name)

        expected = "AI_3"
        self.under_test = AIPlayer(self.brain, self.game_token)
        self.assertEqual(expected, self.under_test.name)

    def test_make_move(self):
        # Mock the brain
        expected = (0, 1)
        board = TicTacToeBoard()

        self.under_test.brain.calculate_next_move = lambda b, gt: expected

        result = self.under_test.make_move(board)
        self.assertIsNotNone(result)
        self.assertTrue(MOVE in result)
        self.assertTrue(GAME_TOKEN in result)
        self.assertEqual(self.game_token, result[GAME_TOKEN])
        self.assertEqual(expected, result[MOVE])
