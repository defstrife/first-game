import pygame
import loot as Loot

class Coin(Loot.Loot):
    def __init__(self, x, y):
        super().__init__(x, y, "coin")
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/coin.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=(x,y))