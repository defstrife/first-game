import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width = 100, height = 100):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/wall.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(center=(x,y))
        self.width = width
        self.height = height