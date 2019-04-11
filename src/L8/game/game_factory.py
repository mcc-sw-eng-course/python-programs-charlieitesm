from argparse import Namespace

from L8.constants.constants import GameName, GameMode
from L8.game.checkers.checkers_game import CheckersLocalGame, CheckersServerGame, CheckersClientGame
from L8.game.game import Game
from L8.game.game_token import TIC_TAC_TOE_TOKENS, CHECKERS_TOKENS
from L8.game.tic_tac_toe.tic_tac_toe_game import TicTacToeLocalGame, TicTacToeServerGame, TicTacToeClientGame
from L8.player.ai.checkers_brain import CheckersBrain
from L8.player.ai.tic_tac_toe_brain import TicTacToeBrain
from L8.player.ai_player import AIPlayer
from L8.player.human_player import HumanPlayer
from L8.player.remote_player import RemotePlayer
from L8.ui.ui import ConsoleUI


class GameFactory:

    @staticmethod
    def build_game(args: Namespace) -> Game:
        players = []
        ui = ConsoleUI()
        tokens = []
        new_game = None
        ai_brain = None

        # 1. Get the appropriate tokens and AI Brain
        if args.game == GameName.TIC_TAC_TOE:
            tokens = TIC_TAC_TOE_TOKENS.copy()
            ai_brain = TicTacToeBrain(args.level)
        elif args.game == GameName.CHECKERS:
            tokens = CHECKERS_TOKENS.copy()
            ai_brain = CheckersBrain(args.level)

        # 2. Build the player instances
        if args.game_mode == GameMode.LOCAL:
            for i in range(args.human_players):
                token_to_assign = tokens.pop(0)
                players.append(HumanPlayer(ui, token_to_assign))

        elif args.game_mode == GameMode.SERVER:
            for i in range(args.human_players):
                token_to_assign = tokens.pop(0)
                players.append(RemotePlayer(token_to_assign))

        elif args.game_mode == GameMode.CLIENT:
            # Client games contain only a local HumanPlayer everything else is provided by the server
            players.append(HumanPlayer(ui, tokens.pop(0)))

        # 3. Build the AI Players, if needed and as many as needed to complete 2 players
        if args.game_mode != GameMode.CLIENT:
            for i in range(len(players), 2):
                token_to_assign = tokens.pop(0)
                players.append(AIPlayer(ai_brain, token_to_assign))

        # Build the game
        if args.game == GameName.TIC_TAC_TOE:
            if args.game_mode == GameMode.LOCAL:
                new_game = TicTacToeLocalGame(players)
            elif args.game_mode == GameMode.SERVER:
                new_game = TicTacToeServerGame(players, args.port)
            elif args.game_mode == GameMode.CLIENT:
                new_game = TicTacToeClientGame(players, args.ip_address, args.port)

        elif args.game == GameName.CHECKERS:
            if args.game_mode == GameMode.LOCAL:
                new_game = CheckersLocalGame(players)
            elif args.game_mode == GameMode.SERVER:
                new_game = CheckersServerGame(players, args.port)
            elif args.game_mode == GameMode.CLIENT:
                new_game = CheckersClientGame(players, args.ip_address, args.port)

        return new_game
