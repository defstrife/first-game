import pygame

class Spike(pygame.sprite.Sprite):
    def __init__(self, x, y, width = 75, height = 75):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/spike.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(center=(x,y))
        self.width = width
        self.height = height