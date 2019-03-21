from L8.board.board import Board


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
