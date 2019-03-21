from L8.board.board import Board
from L8.constants.constants import GAME_TOKEN, MOVE
from L8.game.game_token import GameToken
from L8.messages.english import ENTER_YOUR_MOVE, INVALID_FORMAT_FOR_MOVE
from L8.player.player import Player
from L8.ui.ui import UI


class HumanPlayer(Player):

    PLAYER_NUM = 1

    def __init__(self, ui: UI, game_token: GameToken):
        super().__init__(game_token, ui)

    def generate_name(self) -> str:
        self_name = f"H_P{HumanPlayer.PLAYER_NUM}"
        HumanPlayer.PLAYER_NUM += 1
        return self_name

    def make_move(self, board: Board) -> dict:
        move = self.ui.input(ENTER_YOUR_MOVE).split(",")

        while not move or len(move) != 2 or not all([m.isdigit() for m in move]):
            self.ui.output(INVALID_FORMAT_FOR_MOVE)
            move = self.ui.input(ENTER_YOUR_MOVE).split(",")

        move = (int(move[0]), int(move[1]))

        return {
            GAME_TOKEN: self.game_token,
            MOVE: move
        }
