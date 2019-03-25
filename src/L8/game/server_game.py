import logging
import socket
from abc import ABC

from L8.game.game import Game

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

                self.managed_resources.append(self.server_socket)
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
        pass

    def release_resources(self):
        ServerGame.LOGGER.info(f"Releasing server resources for port... {self.port}")

        for mr in self.managed_resources:
            if mr:
                try:
                    mr.close()
                except:
                    ServerGame.LOGGER.error(f"There was a problem trying to close resoure {str(mr)}")
                    ServerGame.LOGGER.exception("Exception thrown")
