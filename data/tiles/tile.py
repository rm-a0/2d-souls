import pygame
from utils.texture_cache import texture_cache
from core.constants import WHITE

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, tile_id):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        if tile_id in texture_cache:
            self.image.blit(texture_cache[tile_id], (0, 0))
        else:
            self.image.fill(WHITE)
