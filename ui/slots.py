import pygame
import sys

from constants import *

class Slot(pygame.sprite.Sprite):
    def __init__(self, x, y, font): 
        super().__init__()
        self.image = pygame.Surface((SLOT_WIDTH, SLOT_HEIGHT))
        self.image.fill(GREY)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.item = None
        self.font = font

    def switch_item(self, item):
        self.item = item

    def update_count(self):
        self.image.fill(GREY)
        if self.item:
            if hasattr(self.item, "count"):
                count_txt = self.font.render(str(self.item.count), True, WHITE)
                self.image.blit(count_txt, (self.rect.width - 25, self.rect.height - 25))
