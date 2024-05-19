#!usr/bin/env python3
import pygame
from ../constants.py import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, hp, stamina, mana):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 5
