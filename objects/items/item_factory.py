import pygame

from core.constants import *
from objects.items.consumable import Flask

class ItemFactory:
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
