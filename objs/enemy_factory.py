import pygame

from core.const import *
from objs.enemy import Enemy
from objs.weapon import Weapon
from objs.obj_factory import ObjFactory

class EnemyFactory:
    @staticmethod
    def create_basic_enemy(x, y):
        enemy = Enemy(
            x,
            y,
            ENEMY_WIDTH,
            ENEMY_HEIGHT,
            RED,
            ENEMY_MAX_HP,
            ENEMY_SPEED
        )
        weapon = ObjFactory.create_weapon()
        enemy.equip_weapon(weapon)
        return enemy
