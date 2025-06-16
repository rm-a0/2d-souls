import pygame
import os
from core.constants import TILE_WIDTH, TILE_HEIGHT

texture_cache = {}

# Preloads textures for every tile type
def preload_textures():
    tile_types = {
        0: (os.path.join("assets", "textures", "default_texture.png"), (TILE_WIDTH, TILE_HEIGHT))
    }

    for tile_id, (path, size) in tile_types.items():
        try:
            texture = pygame.image.load(path).convert_alpha()
            texture_cache[tile_id] = pygame.transform.scale(texture, size)
        except pygame.error as e:
            print(f"Error loading texture {path}: {e}")
            texture_cache[tile_id] = pygame.Surface(size)
            texture_cache[tile_id].fill((255, 0, 0))
