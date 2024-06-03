import pygame

from core.constants import ENEMY_WIDTH, ENEMY_HEIGHT, RED, ENEMY_MAX_HP, ENEMY_SPEED
from objects.entities.bosses.boss import Boss
from objects.weapons.weapon_factory import WeaponFactory

class BossFactory:
    @staticmethod
    def create_default_boss(x, y):
        boss = Boss(
            x,
            y,
            ENEMY_WIDTH,
            ENEMY_HEIGHT,
            RED,
            ENEMY_MAX_HP,
            ENEMY_SPEED
        )
        weapon = WeaponFactory.create_default_weapon()
        boss.equip_weapon(weapon)
        return boss
