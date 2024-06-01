import os
import pygame

from core.const import *
from objs.enemy_factory import EnemyFactory
from objs.tile_factory import TileFactory

class Level:
    def __init__(self, x, y, base_path):
        self.name = f"lvl_{x}_{y}"
        self.x = x 
        self.y = y
        self.tilemap = []
        self.tiles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bosses = pygame.sprite.Group()
        self.base_path = base_path

    def load_level(self):
        filepath = os.path.join(self.base_path, self.name)
        self.tilemap = self.load_tilemap(os.path.join(filepath, 'tilemap.txt'))
        self.decode_tilemap()

    def load_tilemap(self, path):
        if os.path.exists(path):
            with open(path, 'r') as f:
                tilemap = [line.strip().split(',') for line in f]

                for row in tilemap:
                    row[:] = [int(tile) for tile in row]
                return tilemap
        return []

    def decode_tilemap(self):
        for y, row in enumerate(self.tilemap):
            for x, tile in enumerate(row):
                if tile == 1:
                    self.tiles.add(TileFactory.create_tile(x, y))
                elif tile == 2:
                    self.enemies.add(EnemyFactory.create_enemy(x*tile_width, y*tile_height))
                elif tile == 3:
                    self.bosses.add(EnemyFactory.create_enemy(x*tile_width, y*tile_height))

    def render(self, screen):
        self.tiles.draw(screen)
        self.enemies.draw(screen)
        self.bosses.draw(screen)