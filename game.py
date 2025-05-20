import pygame
import sys

# Constants
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // 3

# Initialize board
board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Initialize pygame
pygame.init()

# Create the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
FONT = pygame.font.SysFont(None, 40)

player = 'X'

def draw_board():
    screen.fill(BG_COLOR)
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)

def draw_points(player1, player2):
    text = FONT.render(f"X: {player1}  O: {player2}", True, (255, 255, 255))
    screen.blit(text, (20, 10))

def draw_marks():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                pygame.draw.line(screen, (66, 66, 66),
                                 (col * SQUARE_SIZE + 55, row * SQUARE_SIZE + 55),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - 55, row * SQUARE_SIZE + SQUARE_SIZE - 55), 25)
                pygame.draw.line(screen, (66, 66, 66),
                                 (col * SQUARE_SIZE + 55, row * SQUARE_SIZE + SQUARE_SIZE - 55),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - 55, row * SQUARE_SIZE + 55), 25)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, (239, 231, 200),
                                   (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                                   SQUARE_SIZE // 3, 15)

def check_win(player):
    # Check rows
    for row in board:
        if all([spot == player for spot in row]):
            return True
    # Check columns
    for col in range(BOARD_COLS):
        if all([board[row][col] == player for row in range(BOARD_ROWS)]):
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(BOARD_ROWS)]):
        return True
    if all([board[i][BOARD_ROWS - i - 1] == player for i in range(BOARD_ROWS)]):
        return True
    return False

# Main loop
while True:
    draw_board()
    draw_points(0, 0)
    draw_marks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if board[clicked_row][clicked_col] is None:
                board[clicked_row][clicked_col] = player

                if check_win(player):
                    print(f"Player {player} wins!")

                player = 'O' if player == 'X' else 'X'

    pygame.display.update()



