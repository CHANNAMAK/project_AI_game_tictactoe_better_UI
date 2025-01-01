import pygame
import sys
from utils import *  # Import utility functions/constants (e.g., screen size, colors, fonts, etc.)
from ai import *     # Import the AI class for decision-making logic
from board import *  # Import the Board class for managing the grid and symbols
from game import *   # Import the Game class that handles overall game flow

# --- Main Program Entry Point ---
if __name__ == "__main__":
    """
    Entry point of the Tic Tac Toe game.
    Initializes the Game class and starts the game loop.
    """
    game = Game()  # Create an instance of the Game class
    game.run()     # Start the game loop
