import pygame
from constants import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 70))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        # Physiscs 
        self.vel_x = 0
        self.vel_y = 0
        # Enemy stats
        self.max_hp = ENEMY_MAX_HP 
        self.max_mana = ENEMY_MAX_MANA
        self.max_stamina = ENEMY_MAX_STAMINA
        self.hp = ENEMY_MAX_HP
        self.mana = ENEMY_MAX_MANA
        self.stamina = ENEMY_MAX_STAMINA
        self.speed = ENEMY_SPEED
