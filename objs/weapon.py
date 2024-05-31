import pygame
from core.const import *

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
    def is_intersecting(self, obj):
        return self.rect.colliderect(obj.rect)

    # Deals damage to an object
    def deal_damage(self, obj):
        if hasattr(obj, 'hp'):
            obj.hp -= self.damage
            if obj.hp <= 0:
                obj.kill()

    # Increase weapon damage by certain ammount
    def increase_damage(self, amt):
        self.damage += amt
