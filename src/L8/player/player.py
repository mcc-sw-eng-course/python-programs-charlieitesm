from abc import abstractmethod, ABC

from L8.board.board import Board
from L8.game.game_token import GameToken
from L8.ui.ui import UI


class Player(ABC):

    def __init__(self, game_token: GameToken, ui: UI):
        self.name = self.generate_name()
        self.ui = ui
        self.game_token = game_token

    @abstractmethod
    def make_move(self, board: Board) -> dict:  # pragma: no cover
        raise NotImplementedError

    @abstractmethod
    def generate_name(self) -> str:  # pragma: no cover
        raise NotImplementedError

    def __str__(self):
        return self.name
