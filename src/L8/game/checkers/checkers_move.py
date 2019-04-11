class CheckersMove:

    def __init__(self, from_row: int, from_col: int, to_row: int, to_col: int) -> None:
        self.fr = from_row
        self.fc = from_col
        self.tc = to_col
        self.tr = to_row

    def __eq__(self, other):
        return (self.fc == other.fc) and (self.fr == other.fr) and (self.tc == other.tc) and (self.tr == other.tr)