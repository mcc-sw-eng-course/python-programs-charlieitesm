from argparse import Namespace
from unittest import TestCase

from L8.constants.constants import GameMode, TypeOfUI, GameName, GameLevel
from L8.game.game import Game
from L8.game.game_factory import GameFactory
from L8.game.local_game import LocalGame
from L8.game.tic_tac_toe.tic_tac_toe_game import TicTacToeGame, TicTacToeLocalGame
from L8.player.ai_player import AIPlayer
from L8.player.human_player import HumanPlayer
from L8.ui.ui import ConsoleUI


class TestGameFactory(TestCase):

    def setUp(self):
        self.args = Namespace()

    def test_build_game(self):

        self.args.__setattr__("game_mode", GameMode.LOCAL)
        self.args.__setattr__("ui", TypeOfUI.CONSOLE)
        self.args.__setattr__("game", GameName.TIC_TAC_TOE)
        self.args.__setattr__("level", GameLevel.EASY)
        self.args.__setattr__("human_players", 1)

        under_test = GameFactory.build_game(self.args)

        self.assertTrue(isinstance(under_test, Game))
        self.assertTrue(isinstance(under_test, LocalGame))
        self.assertTrue(isinstance(under_test, TicTacToeGame))
        self.assertTrue(isinstance(under_test, TicTacToeLocalGame))

        number_of_human_players = 0
        number_of_ai_players = 0
        ai_player = None
        human_player = None

        for p in under_test.players:

            if isinstance(p, HumanPlayer):
                number_of_human_players += 1
                human_player = p
            elif isinstance(p, AIPlayer):
                number_of_ai_players += 1
                ai_player = p

        self.assertTrue(number_of_human_players == 1)
        self.assertTrue(number_of_ai_players == 1)

        self.assertTrue(ai_player.brain.level == GameLevel.EASY)
        self.assertTrue(isinstance(human_player.ui, ConsoleUI))
