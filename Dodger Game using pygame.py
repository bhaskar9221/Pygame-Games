import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dodger Game")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the player character
player_size = 50
player_x = screen_width // 2 - player_size // 2
player_y = screen_height - player_size - 10
player_speed = 5

# Set up the enemy characters
enemy_size = 50
enemy_x = random.randint(0, screen_width - enemy_size)
enemy_y = 0
enemy_speed = 3

# Set up the clock
clock = pygame.time.Clock()

game_over = False

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Get the player's input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_size:
        player_x += player_speed

    # Update enemy position
    enemy_y += enemy_speed
    if enemy_y > screen_height:
        enemy_y = 0
        enemy_x = random.randint(0, screen_width - enemy_size)

    # Check for collision between player and enemy
    if (
        player_x < enemy_x + enemy_size
        and player_x + player_size > enemy_x
        and player_y < enemy_y + enemy_size
        and player_y + player_size > enemy_y
    ):
        game_over = True

    # Clear the screen
    screen.fill(WHITE)

    # Draw the player and enemy
    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_size, enemy_size))

    # Update the display
    pygame.display.flip()

    # Set the frames per second
    clock.tick(60)

# Quit the game
pygame.quit()
