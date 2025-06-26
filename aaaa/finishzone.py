import pygame

class Finishzone(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/portal.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(center=(x,y))
        self.drawzone = False

    def the_end(self, enemies, coins):
        if len(coins) == 0 and len(enemies) == 0:
            self.drawzone = True
        else:
            self.drawzone = False
        return self.drawzone