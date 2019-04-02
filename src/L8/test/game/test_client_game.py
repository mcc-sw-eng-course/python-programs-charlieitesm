import time
from unittest import TestCase
from typing import Any, Iterable, Tuple, List, Optional, Union, overload, TypeVar, Text

from L8.constants.constants import GameLevel
from L8.game.client_game import ClientGame
from L8.game.game_token import GameToken
from L8.game.tic_tac_toe.tic_tac_toe_game import TicTacToeClientGame
from L8.player.ai.tic_tac_toe_brain import TicTacToeBrain
from L8.player.ai_player import AIPlayer
from L8.player.human_player import HumanPlayer
from L8.ui.ui import ConsoleUI


class TestClientGame(TestCase):

    def setUp(self):
        players = [AIPlayer(TicTacToeBrain(GameLevel.EASY), GameToken("X")),
                   AIPlayer(TicTacToeBrain(GameLevel.EASY), GameToken("Y"))]
        self.client = TicTacToeClientGame(players, "127.0.0.1",  8081)
        self.client.server_socket = SampleServer()

    def test_conect_to_server(self):
        with self.assertRaises(OSError):
            self.client.connect_to_server()

        try:
            self.client.connect_to_server()
        except Exception as e:
            self.fail("it raised an exception when it shouldn't have")

    def test_wait_for_start(self):
        self.client.wait_for_game_to_start()
        self.assertIsNotNone(self.client.players[0].game_token)
        self.assertEqual(self.client.players[0].game_token.token_symbol, 'X')

    def test_ask_and_send_move_to_server(self):
        self.client.ask_and_send_move_to_server(self.client.players[0])
        self.assertIsNotNone(self.client.server_socket.sent_message)
        # check if it is a tuple
        move = self.client.server_socket.sent_message.split(',')
        self.assertEqual(2, len(move))
        self.assertTrue(move[0].isdigit())
        self.assertTrue(move[1].isdigit())

    # This tests not error is Raised in the client event though while closing there was one.
    def test_closing(self):
        self.client.managed_resources = []
        self.client.managed_resources.append(SampleResource())
        self.client.release_resources()
        self.client.release_resources()


class SampleResource(): # pragma: no cover

    def __init__(self):
        self.can_close = False

    def close(self):
        if not self.can_close:
            self.can_close = True
            raise OSError


class SampleServer(): # pragma: no cover

    def __init__(self):
        self.message = ""
        self.can_connect = False
        self.try_counter = 0

    def connect(self, address: Union[tuple, str, bytes]):
        if not self.can_connect:
            if self.try_counter == 3:
                self.can_connect = True
            self.try_counter = self.try_counter + 1
            raise IOError


    def recv(self, buffer: int):
        self.prepare_message()
        return self.message.encode()

    def prepare_message(self):
        time.sleep(3)
        self.message = "RDYX"

    def send(self, data: bytes, flags: int = ...) -> int:
        self.sent_message = data.decode()
        pass
