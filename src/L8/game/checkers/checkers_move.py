class CheckersMove:

    def __init__(self, from_row: int, from_col: int, to_row: int, to_col: int, is_jump: bool) -> None:
        self.fr = from_row
        self.fc = from_col
        self.tc = to_col
        self.tr = to_row
        self.jump = is_jump

