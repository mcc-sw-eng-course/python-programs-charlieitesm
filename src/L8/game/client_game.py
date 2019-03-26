import logging
import socket
import time
from abc import ABC

from L8.constants.network_messages import READY_MSG
from L8.game.game import Game

# Create a logger for later troubleshooting

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='tictectoe-engine_network.log')
console = logging.StreamHandler()
console.setLevel(logging.INFO)

logging.getLogger(__name__).addHandler(console)


class ClientGame(Game, ABC):

    LOGGER = logging.getLogger(__name__)

    def initialize_resources(self):
        ClientGame.LOGGER.info(f"Initializing client to connect to {self.ip_address}:{self.port}...")
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.managed_resources.append(self.server_socket)
        self.connect_to_server()
        self.wait_for_game_to_start()

    def connect_to_server(self):
        max_tries = 3
        tries = 0
        connected_to_server = False

        while tries < max_tries:
            tries += 1

            try:
                # self.server_socket.settimeout(10)
                self.server_socket.connect((self.ip_address, self.port))
                connected_to_server = True

                ClientGame.LOGGER.info(f"Connected to {self.ip_address}:{self.port} successfully!")

                # No need to try to connect again, break the trying loop
                break

            except Exception as e:
                ClientGame.LOGGER.warning(f"There was an error when trying to connect to {self.ip_address}:{self.port}")
                ClientGame.LOGGER.warning(f"Remaining tries: {tries}")
                ClientGame.LOGGER.exception("Exception thrown")

                if tries == max_tries:
                    ClientGame.LOGGER.error(f"Max tries to connect to {self.ip_address}:{self.port} exceeded, "
                                            f"aborting...")
                    raise e
        if not connected_to_server:
            raise ConnectionError(f"Couldn't connect to {self.ip_address}:{self.port}, aborting...")

    def wait_for_game_to_start(self):
        is_client_waiting = True

        while is_client_waiting:
            ClientGame.LOGGER.info(f"Client connected, waiting for game server to start...")
            server_response = self.server_socket.recv(2).decode()

            if server_response.startswith(READY_MSG):
                is_client_waiting = False
            else:
                time.sleep(1)

    # noinspection PyBroadException
    def release_resources(self):
        ClientGame.LOGGER.info(f"Releasing server resources for port... {self.port}")

        for mr in self.managed_resources:
            if mr:
                try:
                    mr.shutdown(socket.SHUT_RDWR)
                    mr.close()
                except:
                    ClientGame.LOGGER.error(f"There was a problem trying to close resoure {str(mr)}")
                    ClientGame.LOGGER.exception("Exception thrown")
