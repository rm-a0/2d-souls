import pygame
from constants import *
from objs.entity import Entity

class Enemy(Entity):
    def __init__(self, x, y, width, height, color, hp, speed):
        super().__init__(x, y, width, height, color, hp,speed)
        self.state = IDLE
        # Flags
        self.stop_duration = 0
        self.charge_duration = 0

    # Decreases hp by certain amount
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.kill()

    # FSM for changing changing states
    def update(self, distance):
        if self.stop_duration > 0:
            self.stop_duration -= 1

        if self.state == IDLE:
            if distance < 400:
                self.state = CHASE
            if distance < 100:
                self.state = ATTACK
                self.charge_duration = 100

        elif self.state == ATTACK:
            if self.charge_duration >= 0:
                return
            if distance > 100:
                self.state = CHASE

        elif self.state == CHASE:
            if distance > 400:
                self.state = IDLE 
            elif distance < 100:
                self.state = ATTACK
                self.charge_duration = 100
            elif distance < 400:
                self.state = CHASE

    # Resets velocity
    def idle(self):
        self.vel_x = 0
        self.vel_y = 0

    # Moves into given direction
    def chase(self, direction):
        if self.stop_duration > 0:
            return
        if direction == LEFT:
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

    # Deals damage to object that is intersecting with weapon
    def attack(self, direction, obj):
        if self.stop_duration > 0:
            self.state = IDLE
            return

        if self.charge_duration > 0:
            self.state == ATTACK
            self.charge_duration -= 1
            return

        self.stop_duration = 120
        if direction == RIGHT:
            self.rect.x += self.speed*50
            self.equipped_weapon.draw_weapon(self.rect.x + PLAYER_WIDTH, self.rect.y + PLAYER_HEIGHT/2)
        else:
            self.rect.x -= self.speed*50
            self.equipped_weapon.draw_weapon(self.rect.x - self.equipped_weapon.length, self.rect.y + PLAYER_HEIGHT/2)
        if self.equipped_weapon.is_intersecting(obj):
            if obj.deflect_duration > 0:
                if obj.deflect_duration >= PERFECT_CTR:
                    self.stop_duration += 120
            else:
                damage = self.equipped_weapon.damage
                obj.take_damage(damage)

    # Decides which method should be executed based on state
    def perform_action(self, direction, obj):
        if self.state == ATTACK:
            self.attack(direction, obj)
        elif self.state == CHASE:
            self.chase(direction)
        elif self.state == IDLE:
            self.idle()

