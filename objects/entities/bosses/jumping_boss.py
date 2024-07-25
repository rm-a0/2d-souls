import pygame

from core.constants import *
from objects.entities.entity import Entity
from objects.entities.bosses.boss import Boss

class JumpingBoss(Boss):
    def __init__(self, x, y, width, height, color, hp, speed):
        super().__init__(x, y, width, height, color, hp, speed)

    def change_state(self, dist):
        if self.state == IDLE:
            if dist < 1000:
                self.state = IDLE
            else:
                self.state = IDLE
