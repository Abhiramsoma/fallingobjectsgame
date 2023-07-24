import pygame
import random

# Initialize Pygame
pygame.init()

# Set up game window
WIDTH, HEIGHT = 600, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Objects Game")

# Set up clock for controlling game speed
CLOCK = pygame.time.Clock()

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up fonts
FONT = pygame.font.SysFont(None, 40)

# Set up game objects
PLAYER_SIZE = 50
player_x = WIDTH // 2 - PLAYER_SIZE // 2
player_y = HEIGHT - PLAYER_SIZE
player_speed = 10

OBJECT_SIZE = 30
object_speed = 5

objects = []
for i in range(10):
    x = random.randint(0, WIDTH - OBJECT_SIZE)
    y = random.randint(-HEIGHT, 0)
    objects.append(pygame.Rect(x, y, OBJECT_SIZE, OBJECT_SIZE))

# Set up game loop
running = True
score = 0

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player based on keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_SIZE:
        player_x += player_speed

    # Move objects down the screen
    for obj in objects:
        obj.y += object_speed
        if obj.y > HEIGHT:
            obj.x = random.randint(0, WIDTH - OBJECT_SIZE)
            obj.y = random.randint(-HEIGHT, 0)
            score += 1

    # Check for collisions
    player_rect = pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE)
    for obj in objects:
        if player_rect.colliderect(obj):
            running = False

    # Draw game objects
    WINDOW.fill(BLACK)
    for obj in objects:
        pygame.draw.rect(WINDOW, WHITE, obj)
    pygame.draw.rect(WINDOW, RED, player_rect)

    # Draw score
    score_text = FONT.render(f"Score: {score}", True, WHITE)
    WINDOW.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

    # Limit frame rate
    CLOCK.tick(60)

# Clean up Pygame
pygame.quit()
