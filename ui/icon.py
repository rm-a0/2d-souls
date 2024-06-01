import pygame

from core.constants import ICON_HEIGHT, ICON_WIDTH, GREY

class Icon(pygame.sprite.Sprite):
    def __init__(self, x, y): 
        super().__init__()
        self.image = pygame.Surface((ICON_WIDTH, ICON_HEIGHT))
        self.image.fill(GREY)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
