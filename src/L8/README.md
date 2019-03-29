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
## Design
The main method calls upon a GameFactory, which creates a Game object (created using polymorphism) and calls upon game::play. Game is an interface that defines all of the methods that a game must have. LocalGame is an abstract class that implements only the necessary methods to run a Local game, we could then just implement a ServerGame or ClientGame that initialize network resouces.

We have a TicTacToeGame which is another abstract class that implements the game logic methods for a TicTacToeGame.

With these pieces we can then create a TicTacToeLocalGame which inherits TicTacToeGame and LocalGame. We could reuse LocalGame for a CheckersLocalGame. Board works in a similar fashion, we have a TicTacToeBoard but we could have a Checkers Board.

Player is an interface implemented by AIPlayer and HumanPlayer. AIPlayer has a Brain, which again, is an interface implemented by TicTacToeBrain. This allows us to reuse the AIPlayer for different games by just changing its brain.

Finally, we have UI, which is implemented by ConsoleUI but could also be used by a GUI or a NetworkUI that could notify players over the network of the state of the game and read their inputs.
## Options
> `-h, --help`

show this help message and exit

> `--game-mode, -m {local,client,server}`

The kind of game mode you want to play: A locally hosted game, a client mode to connect to a server, or start a server
so that clients can connect to and play. In client mode, the *--human-players, --game and --level* options are ignored. 
Default: *local*

> `--human-players, -p N`

The number of human players. The rest of the players will be controlled by the CPU. Values can be 0-2. Default: *2*

> `--ui, u {console}`

The type of UI that you want the human players to communicate with. Ignored in server mode. Default: *console*

> `--game, -g {tictactoe}`

Choose the game you want to play. Default: *tictactoe*

> `--level, -l {easy,normal,hard}`

Choose the level of the AI. This argument is ignored if *--human-players* is 2. Default: *hard*

> `--port PORT`

The port on which you want the server to listen for connections or the clients to connect to. Default: *8081*

> `--ip IP`

The IP address the client will connect to. This argument is ignored if game-mode is not client.


## Running a network game
To start a server listening on localhost:8081 with 2 human players you can execute:
```bash
$ python -m L8.tictectoe_engine -m server -p 2 --port 8081
```
Server mode supports AI players, and like a regular local game, you can set the level of the AI too. To run a server
with just one human player and a hard-level AI player run:
```bash
$ python -m L8.tictectoe_engine -m server -p 1 -l hard --port 8081
```
Once the server is running, it will wait for incoming client connections. To connect a client, start another instance of
TicTecToe Engine on client mode. If you want to connect, for example, to a server running on 192.168.100.1:9002 run:
```bash
$ python -m L8.tictectoe_engine -m client --ip 192.168.100.1 --port 9002
```
The game will then being when all players are connected to the server and ready to play.

## Running coverage for L8
First position yourself in the src/ folder and execute the following command
```bash
$ coverage3 run -m unittest discover L8/
```

This will make use of the discover operation of the unittest module to automatically detect all of the unit tests.

#### Generating a report
After running the coverage report, we can then generate a report to the console:
```bash
$ coverage3 report
```
Or we can get a nicely formatted HTML instead:
```bash
$ coverage3 html
```
This will generate an _htmlcov/index.html_ file that, when opened in a browser will have a colored report on coverage.