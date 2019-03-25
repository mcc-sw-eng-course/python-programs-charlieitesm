from abc import ABC

from L8.game.game import Game


class ServerGame(Game, ABC):
    def initialize_resources(self):
        pass

    def release_resources(self):
        pass
