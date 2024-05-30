import pygame

from constants import*
from ui.icons import Icon
from ui.bars import Bar
from ui.slots import Slot

class UiFactory:
    @staticmethod
    def create_hp_bar():
        return Bar()
