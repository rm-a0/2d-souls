import pygame

from core.constants import ENEMY_WIDTH, ENEMY_HEIGHT, ORANGE, ENEMY_MAX_HP, ENEMY_SPEED
from objects.entities.enemies.enemy import Enemy
from objects.weapons.weapon import Weapon
from objects.weapons.weapon_factory import WeaponFactory

class EnemyFactory:
    @staticmethod
    def create_default_enemy(x, y):
        enemy = Enemy(
            x,
            y,
            ENEMY_WIDTH,
            ENEMY_HEIGHT,
            ORANGE,
            ENEMY_MAX_HP,
            ENEMY_SPEED
        )
        weapon = WeaponFactory.create_default_weapon()
        enemy.equip_weapon(weapon)
        return enemy
