import pygame

from core.constants import *
from objects.entities.entity import Entity

class Boss(Entity):
    def __init__(self, x, y, width, height, color, hp, speed):
        super().__init__(x, y, width, height, color, hp, speed)
        # Flags
        self.state = IDLE
        self.charge = 0

    # Resets velocity
    def idle(self):
        self.velocity.x = 0

    # Moves into given direction
    def chase(self, direction):
        if direction == LEFT:
            self.velocity.x -= self.speed
            self.facing = LEFT
        else:
            self.velocity.x += self.speed
            self.facing = RIGHT

    # Deals damage to object that is intersecting with weapon
    def attack(self, direction, obj):
        if direction == RIGHT:
            self.weapon.draw_weapon(self.rect.x + PLAYER_WIDTH, self.rect.y + PLAYER_HEIGHT/2)
        else:
            self.weapon.draw_weapon(self.rect.x - self.weapon.length, self.rect.y + PLAYER_HEIGHT/2)
        if self.weapon.is_intersecting(obj):
            if obj.deflect > 0:
                if obj.deflect >= PERFECT_CTR:
                    self.state = STUN
                    self.stun = 120
            else:
                self.weapon.deal_damage(obj)
                self.state = IDLE
        else:
            self.state = IDLE

    # FSM for changing changing states
    def change_state(self, dist):
        if self.state == IDLE:
            if dist < 1000:
                self.state = CHASE

        elif self.state == CHASE:
            if dist < 100:
                self.state = CHARGE
                self.charge = 100
            elif dist > 1000:
                self.state = IDLE

        elif self.state == CHARGE:
            if self.charge <= 0:
                self.state = ATTACK

        elif self.state == STUN:
            if self.stun <= 0:
                self.state = IDLE

    # Decides which method should be executed based on state
    def perform_action(self, direction, obj):
        if self.state == IDLE:
            self.idle()
        elif self.state == CHASE:
            self.chase(direction)
        elif self.state == CHARGE:
            self.charge -= 1
        elif self.state == ATTACK:
            self.attack(direction, obj)
