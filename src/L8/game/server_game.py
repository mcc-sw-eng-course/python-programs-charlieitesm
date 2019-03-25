import logging
import socket
import time
from abc import ABC

from L8.game.game import Game
from L8.player.remote_player import RemotePlayer
from L8.ui.ui import RemoteUI

# Create a logger for later troubleshooting
logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='tictectoe-engine_network.log')
console = logging.StreamHandler()
console.setLevel(logging.INFO)

logging.getLogger(__name__).addHandler(console)


class ServerGame(Game, ABC):

    LOGGER = logging.getLogger(__name__)

    def initialize_resources(self):
        ServerGame.LOGGER.info(f"Initializing server on port {self.port}")
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.managed_resources.append(self.server_socket)
        self.bind_to_port()
        self.wait_for_players_to_connect()

    def bind_to_port(self):
        max_tries = 3
        tries = 0

        while tries < max_tries:
            tries += 1

            try:
                self.server_socket.bind(("127.0.0.1", self.port))
                ServerGame.LOGGER.info(f"Reserved port {self.port} successfully!")

                self.server_socket.listen(1)
                ServerGame.LOGGER.info(f"Listening on port: {self.port} successfully!")

                # No need to try to connect again, break the trying loop
                break

            except Exception as e:
                ServerGame.LOGGER.warning(f"There was an error when trying to bind to port {self.port}")
                ServerGame.LOGGER.warning(f"Remaining tries: {tries}")
                ServerGame.LOGGER.exception("Exception thrown")

                if tries == max_tries:
                    ServerGame.LOGGER.error("Max tries to bind server port exceeded, aborting...")
                    raise e

    def wait_for_players_to_connect(self):
        # Wait for connections from RemotePlayers only, AI players are ready to play!
        players_pending_to_connect = [p for p in self.players if type(p) is RemotePlayer]
        ServerGame.LOGGER.info("Waiting for players to connect...")

        while players_pending_to_connect:
            connection, client_address = self.server_socket.accept()
            self.managed_resources.append(connection)

            ServerGame.LOGGER.info(f"Received a connection from {str(client_address)}")

            remote_player = players_pending_to_connect.pop(0)
            remote_player.ui = RemoteUI(connection)

            # Wait for connections every second in order to avoid making an airplane out of our computer
            time.sleep(1)

        ServerGame.LOGGER.info("All players are connected, beginning the game GOOD LUCK!...")

    # noinspection PyBroadException
    def release_resources(self):
        ServerGame.LOGGER.info(f"Releasing server resources for port... {self.port}")

        for mr in self.managed_resources:
            if mr:
                try:
                    mr.close()
                except:
                    ServerGame.LOGGER.error(f"There was a problem trying to close resoure {str(mr)}")
                    ServerGame.LOGGER.exception("Exception thrown")
