import pygame

from core.constants import *
from objects.entities.player import Player
from objects.entities.enemies.enemy import Enemy
from objects.weapons.weapon import Weapon
from objects.items.consumable import Flask

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

    @staticmethod
    def create_mana_flask(count):
        return Flask(
            'mana',
            count,
            40
        )

    @staticmethod
    def create_hp_flask(count):
        return Flask(
            'hp',
            count,
            100
        )
