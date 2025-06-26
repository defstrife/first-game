import pygame
import heart as Heart
import coin as Coin


class Barrel(pygame.sprite.Sprite):
    def __init__(self, x, y, loot_type = None, width = 50, height = 50):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/barrel.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(center=(x,y))
        self.width = width
        self.height = height
        self.loot_type = loot_type

    def open(self):
        if self.loot_type == "heart":
            return Heart.Heart(self.rect.centerx, self.rect.centery)
        if self.loot_type == "powerup":
            return PowerUp.PowerUp(self.rect.centerx, self.rect.centery)
        if self.loot_type == "key":
            return Key.Key(self.rect.centerx, self.rect.centery)
        if self.loot_type == "coin":
            return Coin.Coin(self.rect.centerx, self.rect.centery)
        return None