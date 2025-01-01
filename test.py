# # import pygame
# # import sys

# # # Initialize pygame
# # pygame.init()

# # # Constants
# # SCREEN_SIZE = 600
# # GRID_SIZE = 3
# # CELL_SIZE = SCREEN_SIZE // GRID_SIZE
# # LINE_WIDTH = 5
# # CIRCLE_RADIUS = CELL_SIZE // 3
# # CIRCLE_WIDTH = 10
# # CROSS_WIDTH = 15
# # SPACE = CELL_SIZE // 4

# # WHITE = (255, 255, 255)
# # BLACK = (0, 0, 0)
# # RED = (255, 0, 0)
# # BLUE = (0, 0, 255)

# # # Initialize screen
# # screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
# # pygame.display.set_caption("Tic Tac Toe")

# # # Fonts
# # font = pygame.font.Font(None, 50)

# # # Board
# # board = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# # # Player and AI symbols
# # player_symbol = "X"
# # ai_symbol = "O"

# # # Minimax function
# # def minimax(board, depth, is_maximizing):
# #     winner = check_winner()
# #     if winner == player_symbol:
# #         return -1
# #     elif winner == ai_symbol:
# #         return 1
# #     elif is_draw():
# #         return 0

# #     if is_maximizing:
# #         best_score = -float("inf")
# #         for row in range(GRID_SIZE):
# #             for col in range(GRID_SIZE):
# #                 if board[row][col] is None:
# #                     board[row][col] = ai_symbol
# #                     score = minimax(board, depth + 1, False)
# #                     board[row][col] = None
# #                     best_score = max(score, best_score)
# #         return best_score
# #     else:
# #         best_score = float("inf")
# #         for row in range(GRID_SIZE):
# #             for col in range(GRID_SIZE):
# #                 if board[row][col] is None:
# #                     board[row][col] = player_symbol
# #                     score = minimax(board, depth + 1, True)
# #                     board[row][col] = None
# #                     best_score = min(score, best_score)
# #         return best_score

# # # AI move
# # def ai_move():
# #     best_score = -float("inf")
# #     move = None
# #     for row in range(GRID_SIZE):
# #         for col in range(GRID_SIZE):
# #             if board[row][col] is None:
# #                 board[row][col] = ai_symbol
# #                 score = minimax(board, 0, False)
# #                 board[row][col] = None
# #                 if score > best_score:
# #                     best_score = score
# #                     move = (row, col)
# #     if move:
# #         board[move[0]][move[1]] = ai_symbol

# # # Check winner
# # def check_winner():
# #     # Check rows
# #     for row in board:
# #         if row[0] == row[1] == row[2] and row[0] is not None:
# #             return row[0]

# #     # Check columns
# #     for col in range(GRID_SIZE):
# #         if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
# #             return board[0][col]

# #     # Check diagonals
# #     if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
# #         return board[0][0]
# #     if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
# #         return board[0][2]

# #     return None

# # # Check draw
# # def is_draw():
# #     for row in board:
# #         if None in row:
# #             return False
# #     return True

# # # Draw grid
# # def draw_grid():
# #     for x in range(1, GRID_SIZE):
# #         pygame.draw.line(screen, BLACK, (0, x * CELL_SIZE), (SCREEN_SIZE, x * CELL_SIZE), LINE_WIDTH)
# #         pygame.draw.line(screen, BLACK, (x * CELL_SIZE, 0), (x * CELL_SIZE, SCREEN_SIZE), LINE_WIDTH)

# # # Draw symbols
# # def draw_symbols():
# #     for row in range(GRID_SIZE):
# #         for col in range(GRID_SIZE):
# #             if board[row][col] == "X":
# #                 pygame.draw.line(screen, BLUE, (col * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE),
# #                                  ((col + 1) * CELL_SIZE - SPACE, (row + 1) * CELL_SIZE - SPACE), CROSS_WIDTH)
# #                 pygame.draw.line(screen, BLUE, (col * CELL_SIZE + SPACE, (row + 1) * CELL_SIZE - SPACE),
# #                                  ((col + 1) * CELL_SIZE - SPACE, row * CELL_SIZE + SPACE), CROSS_WIDTH)
# #             elif board[row][col] == "O":
# #                 pygame.draw.circle(screen, RED, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2),
# #                                    CIRCLE_RADIUS, CIRCLE_WIDTH)

# # # Display winner or draw
# # def display_message(message):
# #     screen.fill(WHITE)
# #     text = font.render(message, True, BLACK)
# #     text_rect = text.get_rect(center=(SCREEN_SIZE // 2, SCREEN_SIZE // 2))
# #     screen.blit(text, text_rect)
# #     pygame.display.update()
# #     pygame.time.wait(2000)

# # # Main loop
# # def main():
# #     global player_symbol, ai_symbol

# #     running = True
# #     player_turn = True
# #     while running:
# #         for event in pygame.event.get():
# #             if event.type == pygame.QUIT:
# #                 pygame.quit()
# #                 sys.exit()

# #             if event.type == pygame.MOUSEBUTTONDOWN and player_turn:
# #                 mouse_x, mouse_y = event.pos
# #                 row = mouse_y // CELL_SIZE
# #                 col = mouse_x // CELL_SIZE

# #                 if board[row][col] is None:
# #                     board[row][col] = player_symbol
# #                     player_turn = False

# #                     if check_winner():
# #                         display_message(f"Player {player_symbol} Wins!")
# #                         running = False

# #                     elif is_draw():
# #                         display_message("It's a Draw!")
# #                         running = False

# #         if not player_turn and running:
# #             ai_move()
# #             player_turn = True

# #             if check_winner():
# #                 display_message(f"Player {ai_symbol} Wins!")
# #                 running = False

# #             elif is_draw():
# #                 display_message("It's a Draw!")
# #                 running = False

# #         screen.fill(WHITE)
# #         draw_grid()
# #         draw_symbols()
# #         pygame.display.update()

# # if __name__ == "__main__":
# #     main()
# import pygame
# import sys

# # Initialize pygame
# pygame.init()

# # Constants
# SCREEN_SIZE = 600
# GRID_SIZE = 3
# CELL_SIZE = SCREEN_SIZE // GRID_SIZE
# LINE_WIDTH = 5
# CIRCLE_RADIUS = CELL_SIZE // 3
# CIRCLE_WIDTH = 10
# CROSS_WIDTH = 15
# SPACE = CELL_SIZE // 4

# WHITE = (255, 255, 255)
# BLACK = (244,233,205)
# RED = (255, 0, 0)
# BLUE = (0, 0, 255)
# GRAY = (200, 200, 200)

# # Initialize screen
# screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
# pygame.display.set_caption("Tic Tac Toe")

# # Fonts
# font = pygame.font.Font("assets/font/Mermaid1001.ttf", 30)
# small_font = pygame.font.Font("assets/font/Mermaid1001.ttf", 20)


# # Board
# board = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# # Player and AI symbols
# player_symbol = "X"
# ai_symbol = "O"

# def load_image(path, size):
#     image = pygame.image.load(path)
#     return pygame.transform.scale(image, size)

# # Load custom backgrounds and font
# bg_image = load_image("assets/background.jpg", (SCREEN_SIZE, SCREEN_SIZE))
# bg_image_play = load_image("assets/board_game_1.jpg", (SCREEN_SIZE, SCREEN_SIZE))

# # Draw text centered
# def draw_text_centered(text, font, color, surface, x, y):
#     text_obj = font.render(text, True, color)
#     text_rect = text_obj.get_rect(center=(x, y))
#     surface.blit(text_obj, text_rect)
 
# # Draw custom background
# def draw_background(image):
#     screen.blit(image, (0, 0))

# # Display the start menu
# def start_menu():
#     draw_background(bg_image)
#     draw_text_centered("Welcome to Tic Tac Toe", font, BLACK, screen, SCREEN_SIZE // 2, SCREEN_SIZE // 4)
#     draw_text_centered("Press P to Play", small_font, BLACK, screen, SCREEN_SIZE // 2, SCREEN_SIZE // 2)
#     draw_text_centered("Press Q to Quit", small_font, BLACK, screen, SCREEN_SIZE // 2, SCREEN_SIZE // 2 + 50)
#     pygame.display.update()

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_p:
#                     return
#                 elif event.key == pygame.K_q:
#                     pygame.quit()
#                     sys.exit()

# # Choose player symbol
# def choose_symbol():
#     global player_symbol, ai_symbol
#     draw_background(bg_image)
#     draw_text_centered("Choose Your Symbol", font, BLACK, screen, SCREEN_SIZE // 2, SCREEN_SIZE // 4)
#     draw_text_centered("Press X to be first player as X", small_font, BLACK, screen, SCREEN_SIZE // 2, SCREEN_SIZE // 2)
#     draw_text_centered("Press O to be second player as O", small_font, BLACK, screen, SCREEN_SIZE // 2, SCREEN_SIZE // 2 + 50)
#     pygame.display.update()

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_x:
#                     player_symbol = "X"
#                     ai_symbol = "O"
#                     return
#                 elif event.key == pygame.K_o:
#                     player_symbol = "O"
#                     ai_symbol = "X"
#                     return

# # Display the end menu
# def end_menu(message):
#     draw_background(bg_image)
#     draw_text_centered(message, font, BLACK, screen, SCREEN_SIZE // 2, SCREEN_SIZE // 4)
#     draw_text_centered("Press R to Play Again", small_font, BLACK, screen, SCREEN_SIZE // 2, SCREEN_SIZE // 2)
#     draw_text_centered("Press Q to Quit", small_font, BLACK, screen, SCREEN_SIZE // 2, SCREEN_SIZE // 2 + 50)
#     pygame.display.update()

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_r:
#                     return True
#                 elif event.key == pygame.K_q:
#                     pygame.quit()
#                     sys.exit()

# # Check winner
# def check_winner():
#     # Check rows
#     for row in board:
#         if row[0] == row[1] == row[2] and row[0] is not None:
#             return row[0]

#     # Check columns
#     for col in range(GRID_SIZE):
#         if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
#             return board[0][col]

#     # Check diagonals
#     if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
#         return board[0][0]
#     if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
#         return board[0][2]

#     return None

# # Check draw
# def is_draw():
#     for row in board:
#         if None in row:
#             return False
#     return True

# # Minimax function
# def minimax(board, depth, is_maximizing):
#     winner = check_winner()
#     if winner == player_symbol:
#         return -1  # Player wins
#     elif winner == ai_symbol:
#         return 1  # AI wins
#     elif is_draw():
#         return 0  # Draw

#     if is_maximizing:
#         best_score = -float("inf")
#         for row in range(GRID_SIZE):
#             for col in range(GRID_SIZE):
#                 if board[row][col] is None:
#                     board[row][col] = ai_symbol
#                     score = minimax(board, depth + 1, False)
#                     board[row][col] = None
#                     best_score = max(score, best_score)
#         return best_score
#     else:
#         best_score = float("inf")
#         for row in range(GRID_SIZE):
#             for col in range(GRID_SIZE):
#                 if board[row][col] is None:
#                     board[row][col] = player_symbol
#                     score = minimax(board, depth + 1, True)
#                     board[row][col] = None
#                     best_score = min(score, best_score)
#         return best_score


# # AI move
# def ai_move():
#     best_score = -float("inf")
#     move = None
#     for row in range(GRID_SIZE):
#         for col in range(GRID_SIZE):
#             if board[row][col] is None:
#                 board[row][col] = ai_symbol
#                 score = minimax(board, 0, False)
#                 board[row][col] = None
#                 if score > best_score:
#                     best_score = score
#                     move = (row, col)
#     if move:
#         board[move[0]][move[1]] = ai_symbol

# # Draw grid
# def draw_grid():
#     for x in range(1, GRID_SIZE):
#         pygame.draw.line(screen, BLACK, (0, x * CELL_SIZE), (SCREEN_SIZE, x * CELL_SIZE), LINE_WIDTH)
#         pygame.draw.line(screen, BLACK, (x * CELL_SIZE, 0), (x * CELL_SIZE, SCREEN_SIZE), LINE_WIDTH)

# # Draw symbols
# def draw_symbols():
#     for row in range(GRID_SIZE):
#         for col in range(GRID_SIZE):
#             if board[row][col] == "X":
#                 pygame.draw.line(screen, BLUE, (col * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE),
#                                  ((col + 1) * CELL_SIZE - SPACE, (row + 1) * CELL_SIZE - SPACE), CROSS_WIDTH)
#                 pygame.draw.line(screen, BLUE, (col * CELL_SIZE + SPACE, (row + 1) * CELL_SIZE - SPACE),
#                                  ((col + 1) * CELL_SIZE - SPACE, row * CELL_SIZE + SPACE), CROSS_WIDTH)
#             elif board[row][col] == "O":
#                 pygame.draw.circle(screen, RED, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2),
#                                    CIRCLE_RADIUS, CIRCLE_WIDTH)

# # Minimax function (omitted for brevity, same as your version)

# def main():
#     global board
#     while True:
#         start_menu()
#         choose_symbol()

#         # Reset board
#         board = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
#         running = True
#         player_turn = player_symbol == "X"  # Player starts if they choose X

#         # Allow AI to make the first move if the player chooses O
#         if not player_turn:  
#             ai_move()
#             player_turn = True  # Switch to player after AI's first move

#         while running:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()

#                 # Handle player input during their turn
#                 if event.type == pygame.MOUSEBUTTONDOWN and player_turn:
#                     mouse_x, mouse_y = event.pos
#                     row = mouse_y // CELL_SIZE
#                     col = mouse_x // CELL_SIZE

#                     if board[row][col] is None:  # Only allow moves on empty cells
#                         board[row][col] = player_symbol
#                         player_turn = False  # Switch to AI's turn

#                         if check_winner():
#                             running = False
#                             end_menu(f"Player {player_symbol} Wins!")
#                         elif is_draw():
#                             running = False
#                             end_menu("It's a Draw!")

#             # AI's turn
#             if not player_turn and running:
#                 ai_move()
#                 player_turn = True  # Switch back to the player

#                 if check_winner():
#                     running = False
#                     end_menu(f"Player {ai_symbol} Wins!")
#                 elif is_draw():
#                     running = False
#                     end_menu("It's a Draw!")

#             # Draw the game state
#             draw_background(bg_image_play)
#             draw_grid()
#             draw_symbols()
#             pygame.display.update()



# if __name__ == "__main__":
#     main()



import pygame
import sys

# Initialize pygame fonts (required before using fonts)
pygame.init()

# Screen and grid dimensions
SCREEN_SIZE = 600
GRID_SIZE = 3
CELL_SIZE = SCREEN_SIZE // GRID_SIZE
LINE_WIDTH = 5
CIRCLE_RADIUS = CELL_SIZE // 3
CIRCLE_WIDTH = 10
CROSS_WIDTH = 15
SPACE = CELL_SIZE // 4

# Colors
WHITE = (255, 255, 255)
BLACK = (244, 233, 205)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

# Fonts and assets
FONT_PATH = "assets/font/Mermaid1001.ttf"
bg_image = "assets/background.jpg"
bg_image_play = "assets/board_game_1.jpg"

# Fonts
FONT_SIZE = 30
SMALL_FONT_SIZE = 20
font = pygame.font.Font(FONT_PATH, FONT_SIZE)
small_font = pygame.font.Font(FONT_PATH, SMALL_FONT_SIZE)



# --- Classes ---
class Board:
    def __init__(self):
        self.grid = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    def reset(self):
        self.grid = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    def draw(self, screen):
        for x in range(1, GRID_SIZE):
            pygame.draw.line(screen, BLACK, (0, x * CELL_SIZE), (SCREEN_SIZE, x * CELL_SIZE), LINE_WIDTH)
            pygame.draw.line(screen, BLACK, (x * CELL_SIZE, 0), (x * CELL_SIZE, SCREEN_SIZE), LINE_WIDTH)

    def draw_symbols(self, screen):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if self.grid[row][col] == "X":
                    pygame.draw.line(screen, BLUE, (col * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE),
                                     ((col + 1) * CELL_SIZE - SPACE, (row + 1) * CELL_SIZE - SPACE), CROSS_WIDTH)
                    pygame.draw.line(screen, BLUE, (col * CELL_SIZE + SPACE, (row + 1) * CELL_SIZE - SPACE),
                                     ((col + 1) * CELL_SIZE - SPACE, row * CELL_SIZE + SPACE), CROSS_WIDTH)
                elif self.grid[row][col] == "O":
                    pygame.draw.circle(screen, RED, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2),
                                       CIRCLE_RADIUS, CIRCLE_WIDTH)

    def is_draw(self):
        for row in self.grid:
            if None in row:
                return False
        return True

    def check_winner(self):
        # Check rows
        for row in self.grid:
            if row[0] == row[1] == row[2] and row[0] is not None:
                return row[0]
        # Check columns
        for col in range(GRID_SIZE):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] and self.grid[0][col] is not None:
                return self.grid[0][col]
        # Check diagonals
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[0][0] is not None:
            return self.grid[0][0]
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[0][2] is not None:
            return self.grid[0][2]
        return None


class AI:
    def __init__(self, player_symbol, ai_symbol):
        self.player_symbol = player_symbol
        self.ai_symbol = ai_symbol

    def minimax(self, board, depth, is_maximizing):
        winner = board.check_winner()
        if winner == self.player_symbol:
            return -1
        elif winner == self.ai_symbol:
            return 1
        elif board.is_draw():
            return 0

        if is_maximizing:
            best_score = -float("inf")
            for row in range(GRID_SIZE):
                for col in range(GRID_SIZE):
                    if board.grid[row][col] is None:
                        board.grid[row][col] = self.ai_symbol
                        score = self.minimax(board, depth + 1, False)
                        board.grid[row][col] = None
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for row in range(GRID_SIZE):
                for col in range(GRID_SIZE):
                    if board.grid[row][col] is None:
                        board.grid[row][col] = self.player_symbol
                        score = self.minimax(board, depth + 1, True)
                        board.grid[row][col] = None
                        best_score = min(score, best_score)
            return best_score

    def find_best_move(self, board):
        # If the board is empty, place in the center or corner
        if all(all(cell is None for cell in row) for row in board.grid):
            return (1, 1)  # Prefer the center if empty
        
        best_score = -float("inf")
        move = None
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if board.grid[row][col] is None:
                    board.grid[row][col] = self.ai_symbol
                    score = self.minimax(board, 0, False)
                    board.grid[row][col] = None
                    if score > best_score:
                        best_score = score
                        move = (row, col)
        return move



# Load image function
def load_image(path, size):
    return pygame.transform.scale(pygame.image.load(path), size)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        pygame.display.set_caption("Tic Tac Toe")
        self.board = Board()
        self.running = True
        self.player_symbol = "X"
        self.ai_symbol = "O"
        self.ai = AI(self.player_symbol, self.ai_symbol)
        self.bg_image = load_image(bg_image, (SCREEN_SIZE, SCREEN_SIZE))
        self.bg_image_play = load_image(bg_image_play, (SCREEN_SIZE, SCREEN_SIZE))
        self.current_player = "X"

    def draw_background(self):
        self.screen.blit(self.bg_image, (0, 0))

    def draw_background_play(self):
        self.screen.blit(self.bg_image_play, (0, 0))

    def draw_text_centered(self, text, font, color, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect(center=(x, y))
        self.screen.blit(text_obj, text_rect)
    
    # Display the start menu
    def start_menu(self):
        self.draw_background()
        self.draw_text_centered("Welcome to Tic Tac Toe", font, BLACK, SCREEN_SIZE // 2, SCREEN_SIZE // 4)
        self.draw_text_centered("Press P to Play", small_font, BLACK, SCREEN_SIZE // 2, SCREEN_SIZE // 2)
        self.draw_text_centered("Press Q to Quit", small_font, BLACK, SCREEN_SIZE // 2, SCREEN_SIZE // 2 + 50)
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        return
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

    # Choose player symbol
    def choose_symbol(self):
        self.draw_background()
        self.draw_text_centered("Choose Your Symbol", font, BLACK, SCREEN_SIZE // 2, SCREEN_SIZE // 4)
        self.draw_text_centered("Press X to be first player as X", small_font, BLACK, SCREEN_SIZE // 2, SCREEN_SIZE // 2)
        self.draw_text_centered("Press O to be second player as O", small_font, BLACK, SCREEN_SIZE // 2, SCREEN_SIZE // 2 + 50)
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
        self.draw_background()
        self.draw_text_centered(message, font, BLACK, SCREEN_SIZE // 2, SCREEN_SIZE // 4)
        self.draw_text_centered("Press R to Play Again", small_font, BLACK, SCREEN_SIZE // 2, SCREEN_SIZE // 2)
        self.draw_text_centered("Press Q to Quit", small_font, BLACK, SCREEN_SIZE // 2, SCREEN_SIZE // 2 + 50)
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        # Reset display and game state
                        pygame.display.quit()  # Close the display surface
                        pygame.display.init()  # Reinitialize the display
                        self.screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))  # Recreate surface
                        return True
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()



    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and self.current_player == self.player_symbol:
                x, y = event.pos
                row, col = y // CELL_SIZE, x // CELL_SIZE
                if self.board.grid[row][col] is None:
                    self.board.grid[row][col] = self.player_symbol
                    self.current_player = self.ai_symbol

    def ai_turn(self):
        move = self.ai.find_best_move(self.board)
        if move:
            self.board.grid[move[0]][move[1]] = self.ai_symbol
        self.current_player = self.player_symbol

    def check_game_state(self):
        winner = self.board.check_winner()
        if winner:
            self.running = False
            self.end_menu(f"{winner} wins!")
        elif self.board.is_draw():
            self.running = False
            self.end_menu("It's a draw!")

    def run(self):
        while True:  # Allow continuous restarts
            self.start_menu()
            self.choose_symbol()
            
            # Reset board and state
            self.board.reset()
            self.running = True
            self.current_player = "X"  # Default to X starting

            # If the AI is the first player, make its move
            if self.player_symbol == "O":
                self.current_player = self.ai_symbol  # AI moves first
                self.ai_turn()
            
            while self.running:
                self.handle_input()
                if self.current_player == self.ai_symbol:
                    self.ai_turn()
                self.check_game_state()
                self.draw_background()
                self.board.draw(self.screen)
                self.board.draw_symbols(self.screen)
                pygame.display.update()





if __name__ == "__main__":
    game = Game()
    game.run()
