from L8.board.board import Board
from L8.game.game_token import CHECKERS_TOKENS


class CheckersBoard(Board):
    def __init__(self):
        super().__init__()

        for t in CHECKERS_TOKENS:
            if str(t) == "W":
                self.w = t
            elif str(t) == "B":
                self.b = t
            elif str(t) == "KB":
                self.kb = t
            elif str(t) == "KW":
                self.kw = t

        assert self.w is not None and self.b is not None and self.kb is not None and self.kw

        self.init_board()

    def init_board(self):
        # Initialize a 3x3 board with no tokens
        self.current_state = [
            [None, self.w, None, self.w, None, self.w, None, self.w],
            [self.w, None, self.w, None, self.w, None, self.w, None],
            [None, self.w, None, self.w, None, self.w, None, self.w],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [self.b, None, self.b, None, self.b, None, self.b, None],
            [None, self.b, None, self.b, None, self.b, None, self.b],
            [self.b, None, self.b, None, self.b, None, self.b, None]
        ]

    def __str__(self) -> str:
        """
        This will give us a board formatted like this:
           | W |   | W |   | W |   | W
         W |   | W |   | W |   | W |
           | W |   | W |   | W |   | W
           |   |   |   |   |   |   |
           |   |   |   |   |   |   |
         B |   | B |   | B |   | B |
           | B |   | B |   | B |   | B
         B |   | B |   | B |   | B |
        :return: a str representation of the current board
        """
        representation = "\n".join(
            "|".join(["{:^3}".format(str(val)) if val is not None
                      else "{:3}".format("") for val in row]) for row in self.current_state)
        return representation

    def serialize(self) -> str:
        return ",".join([",".join([str(c) if c is not None else "" for c in row]) for row in self.current_state])

    def deserialize(self, serialized_board: str) -> object:
        state = []

        i = 0
        serialized_tokens = [s.upper() for s in serialized_board.split(",")]

        while i < 64:
            row = []

            for st in serialized_tokens[i: i + 8]:
                if not st:
                    row.append(None)
                elif st.upper() == str(self.w):
                    row.append(self.w)
                elif st.upper() == str(self.b):
                    row.append(self.b)
                elif st.upper() == str(self.kw):
                    row.append(self.kw)
                else:
                    row.append(self.kb)

            state.append(row)
            i += 8

        self.current_state = state

        return self
