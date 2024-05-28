import pygame
from constants import *

class Weapon(pygame.sprite.Sprite):
    def __init__(self, damage, weight, length, width):
        super().__init__()
        self.image = pygame.Surface((length, width))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.damage = damage
        self.weight = weight
        self.length = length
        self.width = width

    # Draw weapon on canvas
    def draw_weapon(self, x, y):
        self.rect.topleft = (x, y)

    # Checks if weapon is intersecting with and object
    def is_intersecting(self, object):
        return self.rect.colliderect(object.rect)
