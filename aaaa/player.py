import pygame
import bomb as Bomb

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/character.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.speedx = 0
        self.speedy = 0
        self.width = width
        self.height = height
        self.rect = self.image.get_rect(center=(x,y))
        self.bombs = []
        self.max_bombs = 1

    def move(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def place_bomb(self, bombs):
        if len(bombs) < self.max_bombs:
            bomb = Bomb.Bomb(self.rect.centerx, self.rect.centery)
            bombs.append(bomb)
            self.bombs.append(bomb)