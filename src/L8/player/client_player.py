from L8.player.remote_player import RemotePlayer


class ClientPlayer(RemotePlayer):
    """
    This ClientPlayer is functionally identical to RemotePlayer but it is used to differentiate semantically between
    ClientPlayers and true RemotePlayers
    """

    def generate_name(self) -> str:
        self_name = f"ClientRemote_P{RemotePlayer.PLAYER_NUM}"
        RemotePlayer.PLAYER_NUM += 1
        return self_name
