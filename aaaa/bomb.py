import pygame

class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/bomb.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=(x,y))
        self.timer = 180
        self.exploded = False
        self.explosion_radius = 100
        self.explosion_duration = 90

    def update(self):
        if not self.exploded:
            self.timer -= 1
            if self.timer <= 0:
                self.exploded = True
                return True
        else:
            self.explosion_duration -= 1
        return False

    def draw_explosion(self, screen):
        if self.exploded and self.explosion_duration > 0:
            explosion_surface = pygame.Surface((self.explosion_radius * 2, self.explosion_radius * 2), pygame.SRCALPHA)
            pygame.draw.circle(explosion_surface, (255, 165, 0, 150),
                               (self.explosion_radius, self.explosion_radius),
                               self.explosion_radius)
            screen.blit(explosion_surface,
                        (self.rect.centerx - self.explosion_radius,
                         self.rect.centery - self.explosion_radius))
    def get_explosion_area(self):
        return pygame.Rect(self.rect.centerx - self.explosion_radius
                           , self.rect.centery - self.explosion_radius
                           , self.explosion_radius * 2
                           , self.explosion_radius * 2)