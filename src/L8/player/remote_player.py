from L8.game.game_token import GameToken
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
