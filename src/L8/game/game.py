from abc import abstractmethod, ABC

from L8.board.board import Board
from L8.constants.constants import MOVE, GAME_TOKEN
from L8.game.game_token import GameToken
from L8.messages.english import ILLEGAL_MOVE
from L8.player.player import Player


class Game(ABC):

    def __init__(self, board: Board, players: list):
        self.board = board
        self.players = players
        self.winner = None

    @abstractmethod
    def initialize_resources(self):  # pragma: no cover
        raise NotImplementedError

    @abstractmethod
    def set_up_game(self):  # pragma: no cover
        raise NotImplementedError

    def play(self):  # pragma: no cover
        # This will contain the main game loop
        is_game_over_yet = False

        while not is_game_over_yet:

            # Ask each of the players for their move
            for player in self.players:

                player.ui.output(f"***** {player}'s turn! ******")
                player.ui.output(self.board)
                move = player.make_move(self.board)

                # Check that the move is legal in the context of the board
                while not self.is_valid_move(move, player):
                    player.ui.output(ILLEGAL_MOVE)
                    move = player.make_move(self.board)

                # Apply the player's move to the board since we now know it was legal
                move_x, move_y = move[MOVE]
                self.board.current_state[move_x][move_y] = move[GAME_TOKEN]

                is_game_over_yet = self.is_game_over()

                # If the game has ended, break the player loop which in turn will break the game loop
                if is_game_over_yet:
                    break

        # Leave every concrete game to decide what it need to do after a game is completed
        self.finish_game()
        self.release_resources()

    @abstractmethod
    def is_valid_move(self, move: dict, player: Player) -> bool:  # pragma: no cover
        raise NotImplementedError

    @abstractmethod
    def is_game_over(self) -> bool:  # pragma: no cover
        raise NotImplementedError

    @abstractmethod
    def finish_game(self):  # pragma: no cover
        raise NotImplementedError

    @abstractmethod
    def release_resources(self):  # pragma: no cover
        raise NotImplementedError

    def token_to_player(self, token_str: GameToken) -> Player:
        """
        Get the player holding the game_token represented by token_str
        :param token_str: a str representing the game_token to look for
        :return: a Player holding the game_token represented by token_str, None if no one was found
        """
        for p in self.players:
            if token_str == p.game_token:
                return p
