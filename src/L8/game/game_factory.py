from argparse import Namespace

from L8.constants.constants import GameName, GameMode
from L8.game.game import Game
from L8.game.tic_tac_toe_game import TicTacToeLocalGame, TicTacToeGame
from L8.player.ai.tic_tac_toe_brain import TicTacToeBrain
from L8.player.ai_player import AIPlayer
from L8.player.human_player import HumanPlayer
from L8.ui.ui import ConsoleUI


class GameFactory:

    @staticmethod
    def build_game(args: Namespace) -> Game:
        players = []
        ui = ConsoleUI()
        tokens = []
        new_game = None
        ai_brain = None

        # Get the appropriate tokens
        if args.game == GameName.TIC_TAC_TOE:
            tokens = TicTacToeGame.LEGAL_TOKENS.copy()
            ai_brain = TicTacToeBrain(args.level)

        # Build the player instances
        for i in range(args.human_players):
            token_to_assign = tokens.pop(0)
            players.append(HumanPlayer(ui, token_to_assign))

        # Build the AI Players, if needed and as many as needed to complete 2 players
        for i in range(len(players), 2):
            token_to_assign = tokens.pop(0)
            players.append(AIPlayer(ai_brain, token_to_assign))

        # Build the game
        if args.game == GameName.TIC_TAC_TOE:
            if args.game_mode == GameMode.LOCAL:
                new_game = TicTacToeLocalGame(players)

        return new_game
