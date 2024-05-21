import pygame
from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 70))
        self.image.fill('white')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        # Player stats
        self.hp = PLAYER_HP
        self.mana = PLAYER_MANA
        self.stamina = PLAYER_STAMINA
        self.speed = PLAYER_SPEED
