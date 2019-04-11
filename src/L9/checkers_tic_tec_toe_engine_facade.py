# The following module is just a facade to call L8.TicTecToe for a Checkers
#  game with 2 Human Players on a local machine
from argparse import Namespace

from L8.constants.constants import GameMode, TypeOfUI, GameName, GameLevel
from L8.game.game_factory import GameFactory


def main():
    # Build the pseudo arguments
    args = Namespace()
    args.game_mode = GameMode.LOCAL
    args.ui = TypeOfUI.CONSOLE
    args.game = GameName.CHECKERS
    args.level = GameLevel.EASY
    args.human_players = 2

    game = GameFactory.build_game(args)
    game.play()
    print("SHUTTING DOWN!")


if __name__ == '__main__':
    main()
