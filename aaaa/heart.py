import pygame
import loot as Loot

class Heart(Loot.Loot):
    def __init__(self, x, y, width = 30, height = 30):
        super().__init__(x, y,"heart")
        self.image = pygame.image.load("images/heart.png")
        self.image = pygame.transform.scale(self.image, (width, height))