import logging
import socket
import time
from abc import ABC

from L8.constants.constants import MOVE
from L8.game.game import Game
from L8.messages.english import ILLEGAL_MOVE_MSG, INVALID_FORMAT_FOR_MOVE_MSG
from L8.messages.network_messages import READY_MSG, ASK_MOVE, INVALID_MOVE, ILLEGAL_MOVE, SIMPLE_MSG, FINISH_GAME
# Create a logger for later troubleshooting
from L8.player.player import Player

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='tictectoe-engine_network-client.log')
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
            server_response = self.server_socket.recv(1024).decode()

            if server_response.startswith(READY_MSG):
                is_client_waiting = False
            else:
                time.sleep(1)

    def play(self):  # pragma: no cover
        try:
            # Let the concrete game to decide if it needs to initialize resources (like network connections)
            self.initialize_resources()

            # This will contain the main game loop
            is_game_over_yet = False

            client_player = self.players[0]  # Only the client is in ClientGames, the rest is handled by the server

            while not is_game_over_yet:

                server_message = self.server_socket.recv(1024).decode()
                server_command = server_message[:3]

                if server_command.startswith(ASK_MOVE):
                    self.board.deserialize(server_message[3:])
                    self.ask_and_send_move_to_server(client_player)

                elif server_command.startswith(INVALID_MOVE):
                    self.board.deserialize(server_message[3:])
                    client_player.ui.output(INVALID_FORMAT_FOR_MOVE_MSG)
                    self.ask_and_send_move_to_server(client_player)

                elif server_command.startswith(ILLEGAL_MOVE):
                    # The server will ask separately for a new move, so just print the message
                    client_player.ui.output(ILLEGAL_MOVE_MSG)

                elif server_command.startswith(SIMPLE_MSG):
                    client_player.ui.output(server_message[3:])

                elif server_command.startswith(FINISH_GAME):
                    self.board.deserialize(server_message[3:])
                    is_game_over_yet = True

            # Leave every concrete game to decide what it needs to do after a game is completed
            self.finish_game()
        finally:
            self.release_resources()

    def ask_and_send_move_to_server(self, player: Player):
        player.ui.output(self.board)
        move = player.make_move(self.board)[MOVE]
        self.server_socket.send(f"{move[0]},{move[1]}".encode())

    # noinspection PyBroadException
    def release_resources(self):
        ClientGame.LOGGER.info(f"Releasing server resources for port... {self.port}")

        for mr in self.managed_resources:
            if mr:
                try:
                    # We could use mr.shutdown(socket.SHUT_RDWR)
                    mr.close()
                except:
                    ClientGame.LOGGER.error(f"There was a problem trying to close resoure {str(mr)}")
                    ClientGame.LOGGER.exception("Exception thrown")
