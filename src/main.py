import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# States
MENU = 'MENU'
PLAYING = 'PLAYING'
PAUSED = 'PAUSED'
GAME_OVER = 'GAME_OVER'

# Initialize state
current_state = MENU

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Procedural Dungeon Crawler')

# Clock
clock = pygame.time.Clock()

# Main Menu
def show_menu():
    screen.fill((0, 0, 0))  # Black background
    font = pygame.font.Font(None, 74)
    title_text = font.render('Main Menu', True, (255, 255, 255))
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 4))
    pygame.display.flip()
    wait_for_menu_input()

def wait_for_menu_input():
    while current_state == MENU:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start_game()  # Start the game

# Game Loop
def start_game():
    global current_state
    current_state = PLAYING
    dungeon_grid = [[0 for _ in range(10)] for _ in range(10)]  # Dummy dungeon grid

    while current_state == PLAYING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))  # Clear screen
        draw_dungeon(dungeon_grid)
        render_hud()
        pygame.display.flip()
        clock.tick(FPS)

# Dungeon grid display
def draw_dungeon(grid):
    cell_size = SCREEN_WIDTH // len(grid[0])
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            pygame.draw.rect(screen, (255, 255, 255), (x * cell_size, y * cell_size, cell_size, cell_size), 1)

# HUD rendering
def render_hud():
    font = pygame.font.Font(None, 36)
    hud_text = font.render('Health: 100', True, (255, 255, 255))
    screen.blit(hud_text, (10, 10))

# Main entry point
if __name__ == '__main__':
    show_menu()