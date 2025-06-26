import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y,speedx = 1, speedy = 0, width = 50, height = 50):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = 1
        self.direction = [speedx, speedy]
        self.image = pygame.image.load("images/enemy.png")
        self.image = pygame.transform.scale(self.image, (width, height))

    def move(self):
        self.rect.x += self.direction[0]
        self.rect.y += self.direction[1]

        if self.rect.x <= 50 or self.rect.x >= 750 - self.rect.width:
            self.direction[0] *= -1
        if self.rect.y <= 50 or self.rect.y >= 550 - self.rect.height:
            self.direction[1] *= -1