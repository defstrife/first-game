import pygame

class Loot(pygame.sprite.Sprite):
    def __init__(self, x, y, loot_type, width = 30, height = 30):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect(center=(x,y))
        self.type = loot_type