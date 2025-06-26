import pygame

class PowerUp(Loot):
    def __init__(self, x, y, width = 30, height = 30):
        super().__init__(x, y,"powerup")
        self.image = pygame.image.fill(0, 0, 255)
        self.image = pygame.transform.scale(self.image, (width, height))