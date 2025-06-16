from core.constants import *
from build.tiles.tile import Tile

class TileFactory:
    @staticmethod
    def create_default_tile(x, y):
        return Tile(
            x,
            y,
            TILE_WIDTH,
            TILE_HEIGHT,
            tile_id=0
        )
