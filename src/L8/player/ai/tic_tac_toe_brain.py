import math
import random

from L8.board.board import Board
from L8.board.tic_tac_toe_board import TicTacToeBoard
from L8.constants.constants import GameLevel
from L8.game.game_token import GameToken, TIC_TAC_TOE_TOKENS
from L8.game.tic_tac_toe.tic_tac_toe_game import TicTacToeGameUtil
from L8.player.ai.brain import Brain


class TicTacToeBrain(Brain):

    def __init__(self, level: GameLevel):
        super().__init__(level)

    def easy_mode(self, board: Board, game_token: GameToken) -> tuple:
        possible_moves = board.get_empty_spaces_coordinates()

        move = random.choice(possible_moves)
        return move

    def normal_mode(self, board: Board, game_token: GameToken) -> tuple:
        # Flip a coin and see if the Brain should act intelligently or not this turn
        flip = random.randint(0, 1)

        if flip == 0:
            return self.easy_mode(board, game_token)
        else:
            return self.hard_mode(board, game_token)

    def hard_mode(self, board: Board, game_token: GameToken) -> tuple:
        opponent_token = [t for t in TIC_TAC_TOE_TOKENS if t is not game_token][0]
        minimax_result = self.minimax(board, game_token, opponent_token, is_ais_turn=True)
        move = minimax_result[1]
        return move

    def minimax(self, board: Board,
                my_game_token: GameToken,
                opponent_game_token: GameToken,
                is_ais_turn: bool) -> tuple:
        winning_token = TicTacToeGameUtil.get_winner(board)

        if winning_token:
            if winning_token == my_game_token:
                # The AI won
                return 1, None
            else:
                # The AI lost
                return -1, None

        possible_moves = board.get_empty_spaces_coordinates()

        if not possible_moves and not winning_token:
            # This was a draw
            return 0, None

        if is_ais_turn:  # Maximize this player
            value = -math.inf
            chosen_move = None

            for move in possible_moves:
                # Make a new Board to keep the original intact
                new_board_matrix = [row.copy() for row in board.current_state]
                new_board = TicTacToeBoard()
                new_board.current_state = new_board_matrix

                # Make the move
                new_board.current_state[move[0]][move[1]] = my_game_token

                # Simulate the opponent making a move
                new_value = self.minimax(new_board, my_game_token, opponent_game_token, is_ais_turn=False)[0]

                if new_value > value:
                    value = new_value
                    chosen_move = move

            return value, chosen_move

        else:  # It's the opponents turn, minimize it!
            value = math.inf
            chosen_move = None

            for move in possible_moves:
                # Make a new Board to keep the original intact
                new_board_matrix = [row.copy() for row in board.current_state]
                new_board = TicTacToeBoard()
                new_board.current_state = new_board_matrix

                # Make the move
                new_board.current_state[move[0]][move[1]] = opponent_game_token

                # Simulate the opponent making a move
                new_value = self.minimax(new_board, my_game_token, opponent_game_token, is_ais_turn=True)[0]

                if new_value < value:
                    value = new_value
                    chosen_move = move

            return value, chosen_move
