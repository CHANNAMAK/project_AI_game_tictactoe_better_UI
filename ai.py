from utils import *  # Importing utility functions/constants (like GRID_SIZE, board checks, etc.)


# Define the AI class to implement the minimax algorithm
class AI:
    def __init__(self, player_symbol, ai_symbol):
        """
        Initialize the AI with player and AI symbols.
        :param player_symbol: The symbol used by the human player (e.g., 'X')
        :param ai_symbol: The symbol used by the AI (e.g., 'O')
        """
        self.player_symbol = player_symbol
        self.ai_symbol = ai_symbol

    def minimax(self, board, depth, is_maximizing):
        """
        Minimax algorithm to determine the best move for the AI.
        Recursively evaluates all possible moves to determine the optimal outcome.

        :param board: The current game board
        :param depth: The current depth of the recursion tree
        :param is_maximizing: Boolean indicating whether the AI is trying to maximize or minimize the score
        :return: The score of the board state
        """
        # Base case: Check for a winner or a draw
        winner = board.check_winner()
        if winner == self.player_symbol:  # If the player wins, return a score of -1
            return -1
        elif winner == self.ai_symbol:  # If the AI wins, return a score of 1
            return 1
        elif board.is_draw():  # If the game is a draw, return a score of 0
            return 0

        # Recursive case: Evaluate possible moves
        if is_maximizing:  # AI's turn to maximize the score
            best_score = -float("inf")  # Initialize best score as negative infinity
            for row in range(GRID_SIZE):
                for col in range(GRID_SIZE):
                    if board.grid[row][col] is None:  # Check if the cell is empty
                        board.grid[row][col] = self.ai_symbol  # Try placing the AI's symbol
                        # Recursively call minimax to evaluate the outcome
                        score = self.minimax(board, depth + 1, False)
                        board.grid[row][col] = None  # Undo the move (backtrack)
                        best_score = max(score, best_score)  # Keep track of the highest score
            return best_score
        else:  # Player's turn to minimize the AI's score
            best_score = float("inf")  # Initialize best score as positive infinity
            for row in range(GRID_SIZE):
                for col in range(GRID_SIZE):
                    if board.grid[row][col] is None:  # Check if the cell is empty
                        board.grid[row][col] = self.player_symbol  # Try placing the player's symbol
                        # Recursively call minimax to evaluate the outcome
                        score = self.minimax(board, depth + 1, True)
                        board.grid[row][col] = None  # Undo the move (backtrack)
                        best_score = min(score, best_score)  # Keep track of the lowest score
            return best_score

    def find_best_move(self, board):
        """
        Find the best move for the AI using the minimax algorithm.
        :param board: The current game board
        :return: The best move as a tuple (row, col)
        """
        # Check if the board is empty: If true, choose the center or a default position
        if all(all(cell is None for cell in row) for row in board.grid):
            return (1, 1)  # Prefer the center (row 1, col 1) if the board is empty

        best_score = -float("inf")  # Initialize the best score as negative infinity
        move = None  # Initialize the best move as None

        # Iterate through all cells in the grid
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if board.grid[row][col] is None:  # Check if the cell is empty
                    board.grid[row][col] = self.ai_symbol  # Simulate AI making a move
                    # Evaluate the score for this move using the minimax function
                    score = self.minimax(board, 0, False)
                    board.grid[row][col] = None  # Undo the move (backtrack)
                    
                    # Update the best move if this move has the highest score
                    if score > best_score:
                        best_score = score
                        move = (row, col)

        return move  # Return the best move as a tuple (row, col)
