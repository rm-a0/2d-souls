import pygame
from constants import *

class Slot(pygame.sprite.Sprite):
    def __init__(self, x, y): 
        super().__init__()
        self.image = pygame.Surface((SLOT_WIDTH, SLOT_HEIGHT))
        self.image.fill(GREY)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.tracking = None
