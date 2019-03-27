from L8.board.board import Board
from L8.game.tic_tac_toe.tic_tac_toe_game import TicTacToeGameUtil


class TicTacToeBoard(Board):

    def __init__(self):
        super().__init__()
        self.init_board()

    def init_board(self):
        # Initialize a 3x3 board with no tokens
        self.current_state = [
            [None, None, None] for _ in range(3)
        ]

    def __str__(self) -> str:
        """
        This will give us a board formatted like this:
         X | O | X
         X | X | O
         X | O | O
        :return: a str representation of the current board
        """
        representation = "\n".join(
            "|".join(["{:^3}".format(str(val)) if val is not None
                      else "{:3}".format("") for val in row]) for row in self.current_state)
        return representation

    def serialize(self) -> str:
        return ",".join([",".join([str(c) if c is not None else "" for c in row]) for row in self.current_state])

    def deserialize(self, serialized_board: str) -> object:
        x = TicTacToeGameUtil.get_token_from_str("X")
        o = TicTacToeGameUtil.get_token_from_str("O")
        state = []

        i = 0
        serialized_tokens = [s.upper() for s in serialized_board.split(",")]

        while i < 9:
            row = [None if not e else x if e.upper() == str(x) else o for e in serialized_tokens[i: i + 3]]
            state.append(row)
            i += 3

        self.current_state = state

        return self
