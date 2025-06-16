from core.constants import *
from data.tiles.tile import Tile

class TileFactory:
    @staticmethod
    def create_default_tile(x, y):
        return Tile(x, y, TILE_WIDTH, TILE_HEIGHT, tile_id=0)

    @staticmethod
    def create_ground_tile_01_01(x, y):
        return Tile(x, y, TILE_WIDTH, TILE_HEIGHT, tile_id=1)

    @staticmethod
    def create_ground_tile_01_02(x, y):
        return Tile(x, y, TILE_WIDTH, TILE_HEIGHT, tile_id=2)

    @staticmethod
    def create_ground_tile_01_03(x, y):
        return Tile(x, y, TILE_WIDTH, TILE_HEIGHT, tile_id=3)

    @staticmethod
    def create_ground_tile_02_01(x, y):
        return Tile(x, y, TILE_WIDTH, TILE_HEIGHT, tile_id=4)

    @staticmethod
    def create_ground_tile_02_02(x, y): 
        return Tile(x, y, TILE_WIDTH, TILE_HEIGHT, tile_id=5)

    @staticmethod
    def create_ground_tile_02_03(x, y): 
        return Tile(x, y, TILE_WIDTH, TILE_HEIGHT, tile_id=6)

    @staticmethod
    def create_ground_tile_03_01(x, y): 
        return Tile(x, y, TILE_WIDTH, TILE_HEIGHT, tile_id=7)

    @staticmethod
    def create_ground_tile_03_02(x, y): 
        return Tile(x, y, TILE_WIDTH, TILE_HEIGHT, tile_id=8)

    @staticmethod
    def create_ground_tile_03_03(x, y): 
        return Tile(x, y, TILE_WIDTH, TILE_HEIGHT, tile_id=9)

