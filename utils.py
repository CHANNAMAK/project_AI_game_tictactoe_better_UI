import pygame
import sys

# --- Pygame Initialization ---
pygame.init()  # Initialize Pygame modules, required for fonts and other Pygame functionalities

# --- Screen and Grid Dimensions ---
SCREEN_SIZE = 600  # Overall window size (600x600 pixels)
GRID_SIZE = 3  # Number of cells in a row/column (3x3 grid)
CELL_SIZE = SCREEN_SIZE // GRID_SIZE  # Size of each cell (200x200 pixels in this case)
LINE_WIDTH = 5  # Width of the grid lines
CIRCLE_RADIUS = CELL_SIZE // 3  # Radius for the 'O' symbol
CIRCLE_WIDTH = 10  # Line thickness for the 'O' symbol
CROSS_WIDTH = 15  # Line thickness for the 'X' symbol
SPACE = CELL_SIZE // 4  # Padding space for 'X' symbol to avoid touching cell edges

# --- Colors ---
WHITE = (255, 255, 255)  # White color (RGB)
BASE_COLOR = (244, 233, 205)  # Light beige color for background
RED = (255, 0, 0)  # Red color for the 'O' symbol
BLUE = (0, 0, 255)  # Blue color for the 'X' symbol
GRAY = (200, 200, 200)  # Gray for neutral UI elements if needed

# --- Fonts and Assets ---
FONT_PATH = "assets/font/Mermaid1001.ttf"  # Path to the custom font file
bg_image = "assets/background.jpg"  # Path to the main background image
bg_image_play = "assets/board_game_1.jpg"  # Path to the game board background image

# --- Fonts ---
FONT_SIZE = 30  # Default font size
SMALL_FONT_SIZE = 20  # Smaller font size for instructions
font = pygame.font.Font(FONT_PATH, FONT_SIZE)  # Load the main font with specified size
small_font = pygame.font.Font(FONT_PATH, SMALL_FONT_SIZE)  # Load the smaller font
