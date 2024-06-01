import os
import pygame

from core.constants import *
from objects.entities.enemies.enemy_factory import EnemyFactory
from build.tiles.tile_factory import TileFactory

class Level:
    def __init__(self, x, y):
        self.name = f"lvl_{x}_{y}"
        self.x = x 
        self.y = y
        self.tilemap = []
        self.tiles = pygame.sprite.Group()
        self.enemies = []
        self.bosses = []

    def load_level(self):
        filepath = os.path.join('build/levels', self.name)
        self.tilemap = self.load_tilemap(os.path.join(filepath, 'tilemap.txt'))
        self.decode_tilemap()

    def load_tilemap(self, path):
        print(path)
        if os.path.exists(path):
            with open(path, 'r') as f:
                tilemap = [line.strip().split(',') for line in f]

                for row in tilemap:
                    row[:] = [int(tile) for tile in row]
                return tilemap
        print("path doesnt exist")
        return []

    def decode_tilemap(self):
        for y, row in enumerate(self.tilemap):
            for x, tile in enumerate(row):
                if tile == 1:
                    self.tiles.add(TileFactory.create_tile(x*TILE_WIDTH, y*TILE_HEIGHT))
                elif tile == 2:
                    self.enemies.append(EnemyFactory.create_default_enemy(x*TILE_WIDTH, y*TILE_HEIGHT))
                elif tile == 3:
                    self.bosses.append(EnemyFactory.create_default_enemy(x*TILE_WIDTH, y*TILE_HEIGHT))
