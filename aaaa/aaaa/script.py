import pygame
from  Spike import Spike
import Coin as coin
import Finishzone as finishzone
import Player as player


pygame.init()

WIDTH, HEIGHT = 800, 600
speed = 5
FPS = 60
score = 0
hearts = 2


spikes = [spike.Spike(500, 550), spike.Spike(200, 550), spike.Spike(325, 200)]
coins = [coin.Coin(100, 100), coin.Coin(600, 55), coin.Coin(625, 550)]
finishzone = finishzone.Finishzone(350, 550)

player = player.Player(10, 10, 50, 50)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
running = True
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)

while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d and player.rect.x < WIDTH - player.width:
                player.speedx = speed
            if event.key == pygame.K_a and player.rect.x > 0:
                player.speedx = -speed
            if event.key == pygame.K_w and player.rect.y > 0:
                player.speedy = -speed
            if event.key == pygame.K_s and player.rect.y < HEIGHT -player.height:
                player.speedy = speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_a:
                player.speedx = 0
            if event.key == pygame.K_s or event.key == pygame.K_w:
                player.speedy = 0

    for spike in spikes:
        screen.blit(spike.image, (spike.rect.x, spike.rect.y))
        if player.rect.colliderect(spike.rect):
            font = pygame.font.Font(None, 72)
            score_text = font.render(f"Не молодец", True, (0, 0, 0))
            screen.blit(score_text, (200, 300))
            #running = False
            if hearts > 0:
                player.rect.x = 0
                player.rect.y = 0

    for coin in coins:
        screen.blit(coin.image, (coin.rect.x, coin.rect.y))
        if player.rect.colliderect(coin.rect):
            coins.remove(coin)
            score += 1
    if player.rect.colliderect(finishzone.rect) and score == 3:
        font = pygame.font.Font(None, 72)
        score_text = font.render(f"Молодец", True, (0, 0, 0))
        screen.blit(score_text, (200, 300))
        running = False



    score_text = font.render(f"Score: {score}", True, (0,0,0))
    screen.blit(score_text, (10, 10))
    screen.blit(player.image, (player.rect.x, player.rect.y))
    screen.blit(finishzone.image, (finishzone.rect.x, finishzone.rect.y))
    player.move()
    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()