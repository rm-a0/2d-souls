import pygame
from constants import *

class Bar(pygame.sprite.Sprite):
    def __init__(self, x, y, ammount, color):
        super().__init__()
        self.image = pygame.Surface((ammount, BAR_HEIGHT))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.color = color

    # Resizes ui based of of updated amount
    def update(self, ammount):
        self.image = pygame.Surface((ammount, BAR_HEIGHT))
        self.image.fill(self.color)
