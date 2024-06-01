import pygame

from core.constants import *
from objects.weapons.weapon import Weapon

class WeaponFactory:
    @staticmethod
    def create_default_weapon():
        return Weapon(
            WEAPON_DAMAGE,
            WEAPON_WEIGHT,
            WEAPON_LENGTH,
            WEAPON_WIDTH
        )


