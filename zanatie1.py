import pygame
import random

pygame.init()

WIDTH,HEIGHT = 800, 600

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My First Game")
running = True

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#Игрок
player_size = 50
player_x = WIDTH/2 - player_size/2
player_y = HEIGHT - player_size - 10
player_speed = 5

#Объект
object_size = 30
object_x = random.randint(0,WIDTH - object_size)
object_y = 0
object_speed = 4

score = 0
font = pygame.font.SysFont(None, 36)



clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    object_y += object_speed
    if object_y > HEIGHT:
        object_x = random.randint(0,WIDTH - object_size)
        object_y = 0

    if player_x < object_x + object_size and player_x + player_size > object_x and player_y < object_y + object_size and player_y + player_size > object_y:
        score += 1
        object_x = random.randint(0,WIDTH - object_size)
        object_y = 0

    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, RED, (object_x, object_y, object_size, object_size))

    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit