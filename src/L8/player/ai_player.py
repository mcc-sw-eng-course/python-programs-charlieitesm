from L8.board.board import Board
from L8.constants.constants import GAME_TOKEN, MOVE
from L8.game.game_token import GameToken
from L8.player.ai.brain import Brain
from L8.player.player import Player
from L8.ui.ui import DummyUI


class AIPlayer(Player):

    PLAYER_NUM = 1

    def __init__(self, brain: Brain, game_token: GameToken):
        # An AI doesn't require a UI, so let's use a DummyUI so that the Game can broadcast messages to players but skip
        #  messaging the AIPlayers
        super().__init__(game_token, DummyUI())
        self.brain = brain

    def generate_name(self) -> str:
        self_name = f"AI_{AIPlayer.PLAYER_NUM}"
        AIPlayer.PLAYER_NUM += 1
        return self_name

    def make_move(self, board: Board) -> dict:
        move = self.brain.calculate_next_move(board, self.game_token)

        return {
            GAME_TOKEN: self.game_token,
            MOVE: move
        }
