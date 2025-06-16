import pygame
import os
from core.constants import TILE_WIDTH, TILE_HEIGHT

texture_cache = {}

# Preloads textures for every tile type
def preload_textures():
    tile_types = {
        0: (os.path.join("assets", "textures", "default_texture.png"), (TILE_WIDTH, TILE_HEIGHT)),
        1: (os.path.join("assets", "textures", "ground_01_01.png"), (TILE_WIDTH, TILE_HEIGHT)),
        2: (os.path.join("assets", "textures", "ground_01_02.png"), (TILE_WIDTH, TILE_HEIGHT)),
        3: (os.path.join("assets", "textures", "ground_01_03.png"), (TILE_WIDTH, TILE_HEIGHT)),
        4: (os.path.join("assets", "textures", "ground_02_01.png"), (TILE_WIDTH, TILE_HEIGHT)),
        5: (os.path.join("assets", "textures", "ground_02_02.png"), (TILE_WIDTH, TILE_HEIGHT)),
        6: (os.path.join("assets", "textures", "ground_02_03.png"), (TILE_WIDTH, TILE_HEIGHT)),
        7: (os.path.join("assets", "textures", "ground_03_01.png"), (TILE_WIDTH, TILE_HEIGHT)),
        8: (os.path.join("assets", "textures", "ground_03_02.png"), (TILE_WIDTH, TILE_HEIGHT)),
        9: (os.path.join("assets", "textures", "ground_03_03.png"), (TILE_WIDTH, TILE_HEIGHT))
    }

    for tile_id, (path, size) in tile_types.items():
        try:
            texture = pygame.image.load(path).convert_alpha()
            texture_cache[tile_id] = pygame.transform.scale(texture, size)
        except pygame.error as e:
            print(f"Error loading texture {path}: {e}")
            texture_cache[tile_id] = pygame.Surface(size)
            texture_cache[tile_id].fill((255, 0, 0))
