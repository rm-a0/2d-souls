import pygame
from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 70))
        self.image.fill('green')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        # Player stats
        self.hp = PLAYER_HP
        self.mana = PLAYER_MANA
        self.stamina = PLAYER_STAMINA
        self.speed = PLAYER_SPEED
        # Flags
        self.jumping = False
        self.rolling = False
        self.facing = RIGHT

    def move_right(self):
        self.rect.x += self.speed
        self.facing = RIGHT

    def move_left(self):
        self.rect.x -= self.speed
        self.facing = LEFT

    def jump(self):
        self.rect.y -= self.speed
