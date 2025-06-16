import os
import pygame

from core.constants import *
from objects.entities.enemies.enemy_factory import EnemyFactory
from objects.entities.bosses.boss_factory import BossFactory
from data.tiles.tile_factory import TileFactory

class Level:
    def __init__(self, x, y):
        self.name = f"lvl_{x}_{y}"
        self.x = x 
        self.y = y
        self.tiles = pygame.sprite.Group()
        self.enemies = []
        self.bosses = []

    def load_level(self):
        filepath = os.path.join('data/levels', self.name)
        fullpath = os.path.join(filepath, 'tilemap.txt')
        self.decode_tilemap(self.load_tilemap(fullpath))

    def load_tilemap(self, path):
        if os.path.exists(path):
            with open(path, 'r') as f:
                tilemap = [line.strip().split(',') for line in f]

                for row in tilemap:
                    row[:] = [int(tile) for tile in row]
                return tilemap
        return []

    def decode_tilemap(self, tilemap):
        for y, row in enumerate(tilemap):
            for x, tile in enumerate(row):
                if tile == 1:
                    self.tiles.add(TileFactory.create_default_tile(x*TILE_WIDTH, y*TILE_HEIGHT))
                elif tile == 2:
                    self.enemies.append(EnemyFactory.create_default_enemy(x*TILE_WIDTH, y*TILE_HEIGHT-30))
                elif tile == 3:
                    self.bosses.append(BossFactory.create_default_boss(x*TILE_WIDTH, y*TILE_HEIGHT))
                elif tile == 4:
                    self.bosses.append(BossFactory.create_jumping_boss(x*TILE_WIDTH, y*TILE_HEIGHT))
