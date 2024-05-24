import pygame
from constants import *

class Weapon(pygame.sprite.Sprite):
    def __init__(self, damage, weight):
        super().__init__()
        self.damage = damage
        self.weight = weight