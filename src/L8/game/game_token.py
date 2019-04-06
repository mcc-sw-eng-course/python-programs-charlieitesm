
class GameToken:

    def __init__(self, token_symbol: str):
        self.token_symbol = token_symbol

    def __str__(self):
        return self.token_symbol


TIC_TAC_TOE_TOKENS = [GameToken("X"), GameToken("O")]
CHECKERS_TOKENS = [GameToken("B"), GameToken("W"), GameToken("KB"), GameToken("KW")]
