import pygame
from constants import *
from objs.entity import Entity

class Enemy(Entity):
    def __init__(self, x, y, width, height, color, hp, speed):
        super().__init__(x, y, width, height, color, hp,speed)
        self.state = IDLE
        # Flags
        self.stun = 0
        self.charge = 0

    # Decreases hp by certain amount
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.kill()

    # Resets velocity
    def idle(self):
        self.vel_x = 0
        self.vel_y = 0

    # Moves into given direction
    def chase(self, direction):
        if direction == LEFT:
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

    # Deals damage to object that is intersecting with weapon
    def attack(self, direction, obj):
        if direction == RIGHT:
            self.rect.x += self.speed*50
            self.weapon.draw_weapon(self.rect.x + PLAYER_WIDTH, self.rect.y + PLAYER_HEIGHT/2)
        else:
            self.rect.x -= self.speed*50
            self.weapon.draw_weapon(self.rect.x - self.weapon.length, self.rect.y + PLAYER_HEIGHT/2)
        if self.weapon.is_intersecting(obj):
            if obj.deflect_duration > 0:
                if obj.deflect_duration >= PERFECT_CTR:
                    self.state = STUN
                    self.stun = 120
            else:
                self.weapon.deal_damage(obj)
                self.state = IDLE

        else:
            self.state = IDLE

    # FSM for changing changing states
    def update(self, dist):
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
        elif self.state == STUN:
            self.stun -= 1
