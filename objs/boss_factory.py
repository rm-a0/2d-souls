import pygame

from core.const import *
from objs.boss import Boss

class EnemyFactory:
    @staticmethod
    def create_boss(x, y):
        return Boss(
            x,
            y,
            ENEMY_WIDTH,
            ENEMY_HEIGHT,
            RED,
            ENEMY_MAX_HP,
            ENEMY_SPEED
        )
