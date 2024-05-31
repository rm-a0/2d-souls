import pygame
from core.const import *

class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, hp, speed):
        super().__init__()
        self.image = pygame.Surface((ENEMY_WIDTH, ENEMY_HEIGHT))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        # Physiscs 
        self.vel_x = 0
        self.vel_y = 0
        # Stats
        self.max_hp = hp
        self.hp = hp
        self.speed = speed
        # Items
        self.weapon = None

    # Passes weapon reference
    def equip_weapon(self, weapon):
        self.weapon = weapon
