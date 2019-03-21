from argparse import ArgumentParser

from L8.constants.constants import GameMode, TypeOfUI, GameName, GameLevel
from L8.game.game_factory import GameFactory
from L8.messages.english import SHUTTING_DOWN

VERSION = "v0.1"


def main():
    args = parse_args()
    game = GameFactory.build_game(args)
    game.play()
    print(SHUTTING_DOWN)


def parse_args():
    """Parse args with argparse
    :returns: args
    """
    parser = ArgumentParser(description=f"TicTecToe Engine {VERSION} - A Board Game engine!")

    parser.add_argument('--game-mode', '-m',
                        default='local',
                        choices=['local', 'client', 'server'],
                        help="The kind of game mode you want to play: A locally hosted game, a client mode to connect"
                             "to a server, or start a server so that clients can connect to and play.")

    parser.add_argument('--human-players', '-p',
                        metavar='N',
                        choices=[0, 1, 2],
                        type=int,
                        default=2,
                        help="The number of human players. The rest of the players will be controlled by the CPU.")

    parser.add_argument('--ui', '-u',
                        default='console',
                        choices=['console'],
                        help="The type of UI that you want the human players to communicate with")

    parser.add_argument('--game', '-g',
                        default='tictactoe',
                        choices=['tictactoe'],
                        help="Choose the game you want to play.")

    parser.add_argument('--level', '-l',
                        default='easy',
                        choices=['easy', 'normal', 'hard'],
                        help="Choose the game you want to play.")

    args = parser.parse_args()

    if args.game_mode == "local":
        args.game_mode = GameMode.LOCAL
    elif args.game_mode == "client":
        args.game_mode = GameMode.CLIENT
    else:
        args.game_mode = GameMode.SERVER

    if args.ui == "console":
        args.ui = TypeOfUI.CONSOLE

    if args.game == "tictactoe":
        args.game = GameName.TIC_TAC_TOE

    if args.level == "easy":
        args.level = GameLevel.EASY
    elif args.level == "hard":
        args.level = GameLevel.HARD
    elif args.level == "normal":
        args.level = GameLevel.NORMAL

    return args


if __name__ == '__main__':
    main()
