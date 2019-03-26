import logging
import socket
import time
from abc import ABC

from L8.constants.network_messages import READY_MSG
from L8.game.game import Game
# Create a logger for later troubleshooting
from L8.player.client_player import ClientPlayer
from L8.player.remote_player import RemotePlayer
from L8.ui.ui import ClientUI, RemoteUI

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

        client_player, remote_player = self.get_client_and_remote_players()

        while tries < max_tries:
            tries += 1

            try:
                # self.server_socket.settimeout(10)
                self.server_socket.connect((self.ip_address, self.port))
                connected_to_server = True

                # Add the RemoteUIs to the player so that they can communicate with the server
                client_player.ui = ClientUI(self.server_socket)
                remote_player.ui = RemoteUI(self.server_socket)

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
        client_player = self.get_client_and_remote_players()[0]

        while is_client_waiting:
            server_response = self.server_socket.recv(2)

            if server_response.startswith(READY_MSG):
                desired_position_of_client = int(server_response[1])

                if self.players[desired_position_of_client] is not client_player:
                    # Switch players in the players list so that the client is in the same order as in the server
                    self.players[0], self.players[1] = self.players[1], self.players[0]
                is_client_waiting = False
            else:
                time.sleep(1)

    def get_client_and_remote_players(self) -> tuple:
        client_player = None
        remote_player = None

        for p in self.players:
            if isinstance(p, ClientPlayer):
                client_player = p
            elif isinstance(p, RemotePlayer):
                remote_player = p

        assert client_player is not None
        assert remote_player is not None

        return client_player, remote_player

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
