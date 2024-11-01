"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board):
        return None

    # Initializing counters
    count_x = 0
    count_o = 0

    # Counting X and O
    for row in board:
        for cell in row:
            if cell == "X":
                count_x += 1
            elif cell == "O":
                count_o += 1

    if count_x > count_o:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:  # If the cell is empty, you can make a move there
                actions.add((i,j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):  # Checking if the action is considered valid
        raise ValueError("Invalid action")

    new_board = [row.copy() for row in board]  # Copying the board to preserve original state

    i, j = action

    new_board[i][j] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # There's only three ways X or O can win:
    # - horizontally
    # - vertically
    # -diagonally


    # Checking for winner row-wise
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]

    # Checking for winner column-wise
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not EMPTY:
            return board[0][col]

    # Checking for winner diagonal-wise
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if utility(board) != 0:
        return True

    for row in board:
        if EMPTY in row:
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)

    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):  # If the game is over, return None
        return None

    current_player = player(board)

    # Initialize best action
    best_action = None
    alpha = -math.inf
    beta = math.inf

    if current_player == X:  # Maximizing for X
        best_value = -math.inf
        for action in actions(board):
            value = minimax_value(result(board, action), alpha, beta, False)
            if value > best_value:
                best_value = value
                best_action = action
            alpha = max(alpha, best_value)
    else:  # Minimizing for O
        best_value = math.inf
        for action in actions(board):
            value = minimax_value(result(board, action), alpha, beta, True)
            if value < best_value:
                best_value = value
                best_action = action
            beta = min(beta, best_value)

    return best_action


def minimax_value(board, alpha, beta, is_maximizing):
    """
    Returns the value of the board for Minimax with alpha-beta pruning.
    """
    if terminal(board):
        return utility(board)

    if is_maximizing:  # Maximizing for X
        best_value = -math.inf  # Setting to a very small value
        for action in actions(board):
            value = minimax_value(result(board, action), alpha, beta, False)
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)  # Updating for alpha-beta pruning
            if beta <= alpha:  # Prune
                break
        return best_value
    else:  # Minimizing for O
        best_value = math.inf  # Setting to a very big value
        for action in actions(board):
            value = minimax_value(result(board, action), alpha, beta, True)
            best_value = min(best_value, value)
            beta = min(beta, best_value)  # Updating for alpha-beta pruning
            if beta <= alpha:  # Prune
                break
        return best_value
