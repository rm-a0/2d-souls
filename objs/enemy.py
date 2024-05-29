import pygame
from constants import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((ENEMY_WIDTH, ENEMY_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        # Physiscs 
        self.vel_x = 0
        self.vel_y = 0
        # Enemy stats
        self.max_hp = ENEMY_MAX_HP 
        self.hp = ENEMY_MAX_HP
        self.speed = ENEMY_SPEED
        self.state = IDLE
        # Flags
        self.stop_duration = 0
        # Items
        self.equipped_weapon = None

    # Passes weapon class reference
    def equip_weapon(self, weapon):
        self.equipped_weapon = weapon

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

        elif self.state == ATTACK:
            if distance < 100:
                self.state = ATTACK
            elif distance > 100:
                self.state = CHASE

        elif self.state == CHASE:
            if distance > 400:
                self.state = IDLE 
            elif distance < 100:
                self.state = ATTACK
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
        self.stop_duration = 120
        if direction == RIGHT:
            self.equipped_weapon.draw_weapon(self.rect.x + PLAYER_WIDTH, self.rect.y + PLAYER_HEIGHT/2)
        else:
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

