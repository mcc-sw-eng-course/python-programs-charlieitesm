from abc import ABC, abstractmethod

from L8.board.board import Board
from L8.constants.constants import GameLevel
from L8.game.game_token import GameToken


class Brain(ABC):

    def __init__(self, level: GameLevel):
        self.level = level

        if level == GameLevel.EASY:
            self.calculate_next_move = self.easy_mode
        elif level == GameLevel.HARD:
            self.calculate_next_move = self.hard_mode
        elif level == GameLevel.NORMAL:
            self.calculate_next_move = self.normal_mode
        else:
            raise ValueError("An invalid GameLevel was provided to the Brain!")

    @abstractmethod
    def easy_mode(self, board: Board, game_token: GameToken) -> tuple:  # pragma: no cover
        raise NotImplementedError

    @abstractmethod
    def normal_mode(self, board: Board, game_token: GameToken) -> tuple:  # pragma: no cover
        raise NotImplementedError

    @abstractmethod
    def hard_mode(self, board: Board, game_token: GameToken) -> tuple:  # pragma: no cover
        raise NotImplementedError
