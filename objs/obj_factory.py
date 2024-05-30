import pygame

from constants import *
from objs.player import Player
from objs.enemy import Enemy
from objs.weapon import Weapon
from objs.consumable import Flask

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
    def create_weapon():
        return Weapon(
            WEAPON_DAMAGE,
            WEAPON_WEIGHT,
            WEAPON_LENGTH,
            WEAPON_WIDTH
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







