import pygame

from constants import *
from objs.player import Player
from objs.enemy import Enemy

class ObjFactory:
    @staticmethod
    def create_player():
        return Player(
            100,
            GROUND,
            PLAYER_WIDTH,
            PLAYER_HEIGHT,
            GREEN,
            PLAYER_MAX_HP,
            PLAYER_SPEED,
            PLAYER_MAX_MANA,
            PLAYER_MAX_STAMINA,
            JUMP_SPEED
        )

    @staticmethod
    def create_enemy():
        return Enemy(
            SCREEN_WIDTH - 200,
            GROUND,
            ENEMY_WIDTH,
            ENEMY_HEIGHT,
            RED,
            ENEMY_MAX_HP,
            ENEMY_SPEED
        )


