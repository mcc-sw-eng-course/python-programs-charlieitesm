### Assignment L8 - Game Engine
The code implements the following entities through interfaces and specific concrete implementations
1. Board
    1. TicTacToeBoard
2. Game
    1. LocalGame
    1. TicTacToeGame
3. Player
    1. HumanPlayer
    1. AIPlayer
4. Brain
    1. TicTacToeBrain
5. UI
    1. ConsoleUI
6. GameLevel
    1. Easy
    1. Normal
    1. Hard
We implemented the selection of the game using Python's argparse.

Through a GameFactory we take the args specified by the user and create a specific game.
We can just add a Checkers game at a later date by just implementing a concrete class.

At the root of L8 there is a tictectoe_engine.py which is the main script and handles the parsing of the arguments in a UNIX-like fashion

```bash
$ python -m L8.tictectoe_engine -p 1 -g tictactoe -l easy --ui console -m local
```
The command above will create a tictactoe game with only 1 human player (1 AI player), on level easy, on local mode (no network) and using a console UI.

You can check all of the available options with
```bash
$ python -m L8.tictectoe_engine --help
```

The main method calls upon a GameFactory, which creates a Game object (created using polymorphism) and calls upon game::play. Game is an interface that defines all of the methods that a game must have. LocalGame is an abstract class that implements only the necessary methods to run a Local game, we could then just implement a ServerGame or ClientGame that initialize network resouces.

We have a TicTacToeGame which is another abstract class that implements the game logic methods for a TicTacToeGame.

With these pieces we can then create a TicTacToeLocalGame which inherits TicTacToeGame and LocalGame. We could reuse LocalGame for a CheckersLocalGame. Board works in a similar fashion, we have a TicTacToeBoard but we could have a Checkers Board.

Player is an interface implemented by AIPlayer and HumanPlayer. AIPlayer has a Brain, which again, is an interface implemented by TicTacToeBrain. This allows us to reuse the AIPlayer for different games by just changing its brain.

Finally, we have UI, which is implemented by ConsoleUI but could also be used by a GUI or a NetworkUI that could notify players over the network of the state of the game and read their inputs.