from abc import abstractmethod, ABC


class Board(ABC):

    def __init__(self):
        self.current_state = [[]]

    @abstractmethod
    def init_board(self): # pragma: no cover
        raise NotImplementedError

    @abstractmethod
    def __str__(self) -> str: # pragma: no cover
        raise NotImplementedError

    def get_empty_spaces_coordinates(self) -> list:
        empty_spaces = []  # What are we living for? ♫

        for x, row in enumerate(self.current_state):
            for y, game_token in enumerate(row):
                if game_token is None:
                    empty_spaces.append((x, y))

        return empty_spaces
