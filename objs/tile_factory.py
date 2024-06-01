from core.const import *
from objs.tile import Tile

class TileFactory:
    @staticmethod
    def create_tile(x, y):
        return Tile(
            x*TILE_HEIGHT,
            y*TILE_WIDTH,
            TILE_WIDTH,
            TILE_HEIGHT,
            WHITE
        )
