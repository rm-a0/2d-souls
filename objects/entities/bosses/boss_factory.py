import pygame

from core.constants import ENEMY_WIDTH, ENEMY_HEIGHT, RED, ENEMY_MAX_HP, ENEMY_SPEED
from objects.bosses.boss import Boss

class BossFactory:
    @staticmethod
    def create_default_boss(x, y):
        return Boss(
            x,
            y,
            ENEMY_WIDTH,
            ENEMY_HEIGHT,
            RED,
            ENEMY_MAX_HP,
            ENEMY_SPEED
        )
