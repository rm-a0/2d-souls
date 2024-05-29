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

    # Decreases hp by certain amount
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.kill()

    # FSM for changing changing states
    def update(self, distance):
        if self.state == IDLE:
            if distance < 10:
                self.state = ATTACK
            elif distance < 50:
                self.state = CHASE

        elif self.state == ATTACK:
            if distance < 10:
                self.state = ATTACK
            elif distance > 50:
                self.state = CHASE

        elif self.state == CHASE:
            if distance > 50:
                self.state = IDLE 
            elif distance > 10:
                self.state = CHASE

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

    # Attacks an object
    def attack(self, direction):
        self.vel_x = 0
        self.vel_y = 0

    # Deecides which method should be executed based on state
    def perform_action(self, direction):
        if self.state == ATTACK:
            self.attack(direction)
        elif self.state == CHASE:
            self.chase(direction)
        elif self.state == IDLE:
            self.idle()

