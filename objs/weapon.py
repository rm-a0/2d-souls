import pygame
from constants import *

class Weapon(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, weight):
        super().__init__()
        self.image = pygame.Surface((20, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.damage = damage
        self.weight = weight

    # Checks if weapon is intersecting with and object
    def is_intersecting(self, object):
        return self.rect.colliderect(object.rect)
