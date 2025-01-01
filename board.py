from utils import *  # Import utility functions/constants (e.g., GRID_SIZE, CELL_SIZE, colors, etc.)

# --- Functions ---
def load_image(path, size):
    """
    Load an image from the given file path and resize it.
    :param path: The file path to the image
    :param size: Tuple indicating the desired size (width, height)
    :return: Resized image object
    """
    return pygame.transform.scale(pygame.image.load(path), size)

# --- Classes ---
class Board:
    def __init__(self):
        """
        Initialize the game board as a 2D grid filled with None.
        GRID_SIZE determines the dimensions of the grid (e.g., 3x3 for Tic Tac Toe).
        """
        self.grid = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    def reset(self):
        """
        Reset the game board to its initial empty state.
        """
        self.grid = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    def draw(self, screen):
        """
        Draw the grid lines on the game screen.
        :param screen: The Pygame screen surface where the grid is drawn
        """
        for x in range(1, GRID_SIZE):  # Draw horizontal and vertical lines
            # Draw horizontal lines
            pygame.draw.line(screen, BASE_COLOR, (0, x * CELL_SIZE), (SCREEN_SIZE, x * CELL_SIZE), LINE_WIDTH)
            # Draw vertical lines
            pygame.draw.line(screen, BASE_COLOR, (x * CELL_SIZE, 0), (x * CELL_SIZE, SCREEN_SIZE), LINE_WIDTH)

    def draw_symbols(self, screen):
        """
        Draw the symbols ('X' and 'O') on the game board.
        :param screen: The Pygame screen surface where the symbols are drawn
        """
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if self.grid[row][col] == "X":  # Draw 'X' symbol
                    pygame.draw.line(screen, BLUE, 
                                     (col * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE),
                                     ((col + 1) * CELL_SIZE - SPACE, (row + 1) * CELL_SIZE - SPACE), CROSS_WIDTH)
                    pygame.draw.line(screen, BLUE, 
                                     (col * CELL_SIZE + SPACE, (row + 1) * CELL_SIZE - SPACE),
                                     ((col + 1) * CELL_SIZE - SPACE, row * CELL_SIZE + SPACE), CROSS_WIDTH)
                elif self.grid[row][col] == "O":  # Draw 'O' symbol
                    pygame.draw.circle(screen, RED, 
                                       (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2),
                                       CIRCLE_RADIUS, CIRCLE_WIDTH)

    def is_draw(self):
        """
        Check if the game is a draw by verifying if all cells are filled.
        :return: True if the game is a draw, False otherwise
        """
        for row in self.grid:
            if None in row:  # If any cell is empty, the game is not a draw
                return False
        return True  # All cells are filled, so it's a draw

    def check_winner(self):
        """
        Check if there is a winner on the board.
        :return: The winning symbol ('X' or 'O'), or None if there is no winner
        """
        # Check rows for a winner
        for row in self.grid:
            if row[0] == row[1] == row[2] and row[0] is not None:
                return row[0]  # Return the winning symbol ('X' or 'O')

        # Check columns for a winner
        for col in range(GRID_SIZE):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] and self.grid[0][col] is not None:
                return self.grid[0][col]  # Return the winning symbol

        # Check diagonals for a winner
        # Top-left to bottom-right diagonal
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[0][0] is not None:
            return self.grid[0][0]  # Return the winning symbol
        
        # Top-right to bottom-left diagonal
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[0][2] is not None:
            return self.grid[0][2]  # Return the winning symbol
        
        # No winner found
        return None
