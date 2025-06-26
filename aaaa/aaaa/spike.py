import pygame

class Spike(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("spike.png")
        self.image = pygame.transform.scale(self.image, (150, 200))
        self.rect = self.image.get_rect(center=(x,y))