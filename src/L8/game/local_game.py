from abc import ABC

from L8.game.game import Game
from L8.messages.english import INITIALIZING_LOCAL_GAME, FINISH_LOCAL_GAME


class LocalGame(Game, ABC):

    def initialize_resources(self):
        print(INITIALIZING_LOCAL_GAME)

    def release_resources(self):
        print(FINISH_LOCAL_GAME)
