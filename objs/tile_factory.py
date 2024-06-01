from core.const import *
from objs.tile import Tile

class TileFactory:
    @staticmethod
    def create_tile(x, y):
        return Tile(
            x*40,
            y*40,
            40,
            40,
            WHITE
        )
