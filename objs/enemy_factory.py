import pygame

from core.const import *
from objs.enemy import Enemy

class EnemyFactory:
    @staticmethod
    def create_enemy(x, y):
        return Enemy(
            x,
            y,
            ENEMY_WIDTH,
            ENEMY_HEIGHT,
            RED,
            ENEMY_MAX_HP,
            ENEMY_SPEED
        )
