from L8.board.checkers_board import CheckersBoard
from L8.game.checkers.checkers_constans import CheckerColors
from L8.game.checkers.checkers_move import CheckersMove
from L8.game.game_token import CHECKERS_TOKENS


class CheckerGameUtil:

    @staticmethod
    def check_if_game_is_over(board: CheckersBoard) -> bool:
        white_movements = CheckerGameUtil.get_valid_moves_for_player(board, board.w)
        black_movements = CheckerGameUtil.get_valid_moves_for_player(board, board.b)
        return len(white_movements) is 0 or len(black_movements) is 0

    @staticmethod
    def is_valid_move(move: CheckersMove, player_color: str, board: CheckersBoard) -> bool:
        """
        Checks if move is a legal move by obtaining a list of legal moves and checking if the move is in the list.
        :param move:
        :param player_color:
        :param board:
        :return: True if it is legal, false otherwise
        """
        legal_moves = CheckerGameUtil.get_valid_moves_for_player(board, player_color)
        return move in legal_moves

    @staticmethod
    def get_valid_moves_for_player(board: CheckersBoard, player_color: str) -> list:
        """
        This method gets a list of legal moves
        :param board:
        :param player_color:
        :return: a list of legal moves
        """
        legal_moves = []
        if player_color is CHECKERS_TOKENS[1]:
            player_king = board.kw
        else:
            player_king = board.kb
        current_state = board.current_state

        # First it checks if the player can jump
        for r, row in enumerate(current_state):
            for c, col in enumerate(row):
                if current_state[r][c] is player_color or current_state[r][c] is player_king:
                    if CheckerGameUtil.can_jump(player_color, r, c, r + 1, c + 1, r + 2, c + 2, board):
                        move = CheckersMove(r, c, r + 2, c + 2)
                        move.is_jump = True
                        move.jumped_enemy_col = c + 1
                        move.jumped_enemy_row = r + 1
                        legal_moves.append(move)
                    if CheckerGameUtil.can_jump(player_color, r, c, r - 1, c - 1, r - 2, c - 2, board):
                        move = CheckersMove(r, c, r - 2, c - 2)
                        move.is_jump = True
                        move.jumped_enemy_row = r - 1
                        move.jumped_enemy_col = c - 1
                        legal_moves.append(move)
                    if CheckerGameUtil.can_jump(player_color, r, c, r + 1, c - 1, r + 2, c - 2, board):
                        move = CheckersMove(r, c, r + 2, c - 2)
                        move.is_jump = True
                        move.jumped_enemy_row = r + 1
                        move.jumped_enemy_col = c - 1
                        legal_moves.append(move)

                    if CheckerGameUtil.can_jump(player_color, r, c, r - 1, c - 1, r - 2, c - 2, board):
                        move = CheckersMove(r, c, r - 2, c - 2)
                        move.is_jump = True
                        move.jumped_enemy_col = c - 1
                        move.jumped_enemy_row = r - 1
                        legal_moves.append(move)

        # if legal_moves has any item, that means the player is forced to jump, so not other kind of move is legal.
        # we check moves without jumps.
        if len(legal_moves) is 0:
            for r, row in enumerate(current_state):
                for c, col in enumerate(row):
                    if current_state[r][c] is player_color or current_state[r][c] is player_king:
                        if CheckerGameUtil.can_move(player_color, r, c, r + 1, c + 1, board):
                            legal_moves.append(CheckersMove(r, c, r + 1, c + 1))
                        if CheckerGameUtil.can_move(player_color, r, c, r - 1, c + 1, board):
                            legal_moves.append(CheckersMove(r, c, r - 1, c + 1))
                        if CheckerGameUtil.can_move(player_color, r, c, r + 1, c - 1, board):
                            legal_moves.append(CheckersMove(r, c, r + 1, c - 1))
                        if CheckerGameUtil.can_move(player_color, r, c, r - 1, c - 1, board):
                            legal_moves.append(CheckersMove(r, c, r - 1, c - 1))
        return legal_moves

    @staticmethod
    def get_jumps_from_position(player_color, r, c, board: CheckersBoard) -> list:
        current_state = board.current_state
        legal_jumps = []
        if player_color is CHECKERS_TOKENS[1]:
            player_king = board.kw
        else:
            player_king = board.kb
        if current_state[r][c] is player_color or current_state[r][c] is player_king:
            if CheckerGameUtil.can_jump(player_color, r, c, r + 1, c + 1, r + 2, c + 2, board):
                move = CheckersMove(r, c, r + 2, c + 2)
                move.is_jump = True
                move.jumped_enemy_col = c + 1
                move.jumped_enemy_row = r + 1
                legal_jumps.append(move)
            if CheckerGameUtil.can_jump(player_color, r, c, r - 1, c - 1, r - 2, c - 2, board):
                move = CheckersMove(r, c, r - 2, c - 2)
                move.is_jump = True
                move.jumped_enemy_row = r - 1
                move.jumped_enemy_col = c - 1
                legal_jumps.append(move)
            if CheckerGameUtil.can_jump(player_color, r, c, r + 1, c - 1, r + 2, c - 2, board):
                move = CheckersMove(r, c, r + 2, c - 2)
                move.is_jump = True
                move.jumped_enemy_row = r + 1
                move.jumped_enemy_col = c - 1
                legal_jumps.append(move)

            if CheckerGameUtil.can_jump(player_color, r, c, r - 1, c - 1, r - 2, c - 2, board):
                move = CheckersMove(r, c, r - 2, c - 2)
                move.is_jump = True
                move.jumped_enemy_col = c - 1
                move.jumped_enemy_row = r - 1
                legal_jumps.append(move)
        return legal_jumps

    @staticmethod
    def can_jump(player_color: str, r1, c1, r2, c2, r3, c3, board: CheckersBoard) -> bool:
        """
        Determines if a piece can make a jump, from row1(r1) and column1(c1) to
        r3,c3. To be able to jump, r3 and c3 must be 2 rows and 2 columns distant
        from r1,c1. r2,c2, must be between r1,c1, and r3,c3. it should contain
        an enemy piece.
        :param player_color:
        :param r1: current row of the piece
        :param c1: current column of the piece
        :param r2: enemy row
        :param c2: enemy column
        :param r3: destination row
        :param c3: destination column
        :param board: used to check current status
        :return: True if the jump is valid, false otherwise.
        """
        if r3 < 0 or r3 >= 8 or c3 < 0 or c3 >= 8:
            return False

        current_state = board.current_state

        if current_state[r3][c3] is not None:
            return False

        if player_color == CHECKERS_TOKENS[1]:
            if current_state[r1][c1] is board.w and r3 < r1:
                return False  # white pieces can only move down
            if current_state[r2][c2] is not board.b and current_state[r2][c2] is not board.kb:
                return False  # there is not a black piece to jump
            return True
        else:
            if current_state[r1][c1] is board.b and r3 > r1:
                return False  # black pieces can only move up
            if current_state[r2][c2] is not board.w and current_state[r2][c2] is not board.kw:
                return False  # there is not a white piece to jump
            return True

    @staticmethod
    def can_move(player_color: str, r1, c1, r2, c2, cb: CheckersBoard):
        if r2 < 0 or r2 >= 8 or c2 < 0 or c2 >= 8:
            return False  # is off the board
        board = cb.current_state

        if board[r2][c2] is not None:
            return False  # there is already a piece in the destination
        if player_color is CHECKERS_TOKENS[0]:
            if board[r1][c1] is cb.w and r2 > r1:
                return False  # regular white piece can only move down
            return True
        else:
            if board[r1][c1] is cb.b and r2 < r1:
                return False  # regular black piece can only move up
            return True
