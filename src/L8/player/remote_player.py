from L8.board.board import Board
from L8.constants.constants import GAME_TOKEN, MOVE
from L8.game.game_token import GameToken
from L8.messages.network_messages import ASK_MOVE, INVALID_MOVE
from L8.player.human_player import HumanPlayer
from L8.ui.ui import UI


class RemotePlayer(HumanPlayer):
    PLAYER_NUM = 1

    def __init__(self, game_token: GameToken):
        # The RemoteUI will be set after the player connects, so let's keep it None for now
        ui: UI = None
        super().__init__(ui, game_token)

    def generate_name(self) -> str:
        self_name = f"Remote_P{RemotePlayer.PLAYER_NUM}"
        RemotePlayer.PLAYER_NUM += 1
        return self_name

    def make_move(self, board: Board) -> dict:
        move = self.ui.input(f"{ASK_MOVE}{board.serialize()}").split(",")

        while not move or len(move) != 2 or not all([m.isdigit() for m in move]):
            move = self.ui.input(f"{INVALID_MOVE}{board.serialize()}").split(",")

        move = (int(move[0]), int(move[1]))

        return {
            GAME_TOKEN: self.game_token,
            MOVE: move
        }

