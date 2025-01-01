import pygame
import sys
from utils import *  # Import utility functions/constants (e.g., SCREEN_SIZE, colors, fonts, etc.)
from ai import *     # Import the AI class for decision-making
from board import *  # Import the Board class for managing game logic


# --- Game Class ---
class Game:
    def __init__(self):
        """
        Initialize the game settings, including screen, board, player symbols, AI, and background images.
        """
        self.screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))  # Set game window size
        pygame.display.set_caption("Tic Tac Toe")  # Set game window title
        self.board = Board()  # Initialize the game board
        self.running = True  # Flag to control the game loop
        self.player_symbol = "X"  # Default player symbol
        self.ai_symbol = "O"  # Default AI symbol
        self.ai = AI(self.player_symbol, self.ai_symbol)  # Initialize AI with player and AI symbols
        self.bg_image = load_image(bg_image, (SCREEN_SIZE, SCREEN_SIZE))  # Load the main background image
        self.bg_image_play = load_image(bg_image_play, (SCREEN_SIZE, SCREEN_SIZE))  # Load the in-game background
        self.current_player = "X"  # Set the starting player to 'X'

    def draw_background(self):
        """
        Draw the main menu background image on the screen.
        """
        self.screen.blit(self.bg_image, (0, 0))

    def draw_background_play(self):
        """
        Draw the in-game background image on the screen.
        """
        self.screen.blit(self.bg_image_play, (0, 0))

    def draw_text_centered(self, text, font, color, x, y):
        """
        Draw text centered at a specific position on the screen.
        :param text: The text to display
        :param font: Font object to render the text
        :param color: Color of the text
        :param x: X-coordinate of the center position
        :param y: Y-coordinate of the center position
        """
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect(center=(x, y))
        self.screen.blit(text_obj, text_rect)
    
    # --- Menu Methods ---
    def start_menu(self):
        """
        Display the start menu with options to play or quit.
        """
        self.draw_background()
        self.draw_text_centered("Welcome to Tic Tac Toe", font, BASE_COLOR, SCREEN_SIZE // 2, SCREEN_SIZE // 4)
        self.draw_text_centered("Press P to Play", small_font, BASE_COLOR, SCREEN_SIZE // 2, SCREEN_SIZE // 2)
        self.draw_text_centered("Press Q to Quit", small_font, BASE_COLOR, SCREEN_SIZE // 2, SCREEN_SIZE // 2 + 50)
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:  # Start the game
                        return
                    elif event.key == pygame.K_q:  # Quit the game
                        pygame.quit()
                        sys.exit()

    def choose_symbol(self):
        """
        Allow the player to choose their symbol ('X' or 'O').
        """
        self.draw_background()
        self.draw_text_centered("Choose Your Symbol", font, BASE_COLOR, SCREEN_SIZE // 2, SCREEN_SIZE // 4)
        self.draw_text_centered("Press X to be first player as X", small_font, BASE_COLOR, SCREEN_SIZE // 2, SCREEN_SIZE // 2)
        self.draw_text_centered("Press O to be second player as O", small_font, BASE_COLOR, SCREEN_SIZE // 2, SCREEN_SIZE // 2 + 50)
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        self.player_symbol = "X"
                        self.ai_symbol = "O"
                        return
                    elif event.key == pygame.K_o:
                        self.player_symbol = "O"
                        self.ai_symbol = "X"
                        return

    def end_menu(self, message):
        """
        Display the end game menu with options to restart or quit.
        :param message: The message to display (e.g., winner or draw message)
        """
        self.draw_background()
        self.draw_text_centered(message, font, BASE_COLOR, SCREEN_SIZE // 2, SCREEN_SIZE // 4)
        self.draw_text_centered("Press R to Play Again", small_font, BASE_COLOR, SCREEN_SIZE // 2, SCREEN_SIZE // 2)
        self.draw_text_centered("Press Q to Quit", small_font, BASE_COLOR, SCREEN_SIZE // 2, SCREEN_SIZE // 2 + 50)
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # Restart the game
                        # Reset display and game state
                        pygame.display.quit()
                        pygame.display.init()
                        self.screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
                        return True
                    elif event.key == pygame.K_q:  # Quit the game
                        pygame.quit()
                        sys.exit()

    # --- Game Logic Methods ---
    def handle_input(self):
        """
        Handle player input (mouse clicks) to make moves.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and self.current_player == self.player_symbol:
                x, y = event.pos  # Get mouse position
                row, col = y // CELL_SIZE, x // CELL_SIZE  # Convert position to grid coordinates
                if self.board.grid[row][col] is None:  # Check if cell is empty
                    self.board.grid[row][col] = self.player_symbol
                    self.current_player = self.ai_symbol  # Switch to AI's turn

    def ai_turn(self):
        """
        Execute the AI's move using the minimax algorithm.
        """
        move = self.ai.find_best_move(self.board)
        if move:  # If a valid move is found
            self.board.grid[move[0]][move[1]] = self.ai_symbol
        self.current_player = self.player_symbol  # Switch back to player's turn

    def check_game_state(self):
        """
        Check if there is a winner or if the game is a draw.
        If the game ends, display the end menu.
        """
        winner = self.board.check_winner()
        if winner:
            self.running = False
            self.end_menu(f"{winner} wins!")  # Display winner message
        elif self.board.is_draw():
            self.running = False
            self.end_menu("It's a draw!")  # Display draw message

    # --- Main Game Loop ---
    def run(self):
        """
        Run the main game loop, including menus, game reset, and gameplay logic.
        """
        while True:  # Allow continuous restarts
            self.start_menu()  # Display start menu
            self.choose_symbol()  # Allow player to choose their symbol
            
            # Reset board and game state
            self.board.reset()
            self.running = True
            self.current_player = "X"  # Default to player 'X' starting

            # If the player chooses 'O', AI makes the first move
            if self.player_symbol == "O":
                self.current_player = self.ai_symbol
                self.ai_turn()
            
            # Gameplay loop
            while self.running:
                self.handle_input()  # Handle player input
                if self.current_player == self.ai_symbol:
                    self.ai_turn()  # AI makes its move
                self.check_game_state()  # Check for winner or draw
                self.draw_background_play()  # Draw updated background
                self.board.draw(self.screen)  # Draw grid
                self.board.draw_symbols(self.screen)  # Draw X and O symbols
                pygame.display.update()  # Refresh the screen
