import pygame
import sys

BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // 3
board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

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
                                   SQUARE_SIZE//3, 15)


# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)

# Create the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
FONT = pygame.font.SysFont(None, 40)

def draw_points(player1, player2):
    text = FONT.render(f"X: {player1}  O: {player2}", True, (255, 255, 255))
    screen.blit(text, (20, 10))


# Draw the board
def draw_board():
    screen.fill(BG_COLOR)
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)

draw_board()
draw_points(0, 0)

draw_board()
draw_points(0, 0)
draw_marks()

player = 'X'

def check_win(player):
    for row in board:
        if all([spot == player for spot in row]):
            return True
    for col in range(BOARD_COLS):
        if all([board[row][col] == player for row in range(BOARD_ROWS)]):
            return True
    if all([board[i][i] == player for i in range(BOARD_ROWS)]):
        return True
    if all([board[i][BOARD_ROWS - i - 1] == player for i in range(BOARD_ROWS)]):
        return True
    return False
if check_win('X'):
    print("Player X wins!")
elif check_win('O'):
    print("Player O wins!")


# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouseX = event.pos[0]
        mouseY = event.pos[1]

        clicked_row = mouseY // SQUARE_SIZE
        clicked_col = mouseX // SQUARE_SIZE

        if board[clicked_row][clicked_col] is None:
            board[clicked_row][clicked_col] = player
            player = 'O' if player == 'X' else 'X'






