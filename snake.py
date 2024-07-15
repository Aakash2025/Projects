import pygame
import random

pygame.init()

# Creating Window
screen_width = 800
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game title
pygame.display.set_caption("Snake Game")
pygame.display.update()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Game specific variables
exit_game = False
game_over = False
snake_x = 100
snake_y = 100
velocity_x = 0
velocity_y = 0
snake_size = 20
food_x = random.randint(20, screen_width - 20 - snake_size)
food_y = random.randint(20, screen_height - 20 - snake_size)

score = 0
init_velocity = 3
fps = 60

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

snk_list = []
snk_length = 1

# Creating a game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and velocity_x == 0:
                velocity_x = init_velocity
                velocity_y = 0
            if event.key == pygame.K_LEFT and velocity_x == 0:
                velocity_x = -init_velocity
                velocity_y = 0
            if event.key == pygame.K_UP and velocity_y == 0:
                velocity_y = -init_velocity
                velocity_x = 0
            if event.key == pygame.K_DOWN and velocity_y == 0:
                velocity_y = init_velocity
                velocity_x = 0

    snake_x += velocity_x
    snake_y += velocity_y

    # Check for collision with food
    if (snake_x < food_x + snake_size and
        snake_x + snake_size > food_x and
        snake_y < food_y + snake_size and
        snake_y + snake_size > food_y):
        score += 1
        food_x = random.randint(20, screen_width - 20 - snake_size)
        food_y = random.randint(20, screen_height - 20 - snake_size)
        snk_length += 5

    # Fill the game window with white color
    gameWindow.fill(white)
    text_screen("Score : " + str(score * 10), red, 5, 5)
    pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

    # Snake head and body logic
    head = [snake_x, snake_y]
    snk_list.append(head)
    if len(snk_list) > snk_length:
        del snk_list[0]

    # Check for collisions with self
    for segment in snk_list[:-1]:
        if segment == head:
            game_over = True

    # Check for collisions with boundaries
    if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0:
        game_over = True

    if game_over:
        text_screen("Game Over! Score: " + str(score * 10), red, screen_width / 6, screen_height / 3)
        pygame.display.update()
        pygame.time.delay(2000)
        exit_game = True
    else:
        plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()

    clock.tick(fps)

pygame.quit()
quit()
