import pygame

class Key(Loot):
    def __init__(self, x, y, width = 30, height = 30):
        super().__init__(x, y,"key")
        self.image = pygame.image.load("images/key.png")
        self.image = pygame.transform.scale(self.image, (width, height))