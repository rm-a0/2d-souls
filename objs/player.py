import pygame
from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 70))
        self.image.fill('green')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        # Physics
        self.vel_x = 0
        self.vel_y = 0
        # Player stats
        self.hp = PLAYER_HP
        self.mana = PLAYER_MANA
        self.stamina = PLAYER_STAMINA
        self.speed = PLAYER_SPEED
        self.jump_speed = JUMP_SPEED
        # Flags
        self.jumping = False
        self.rolling = False
        self.facing = RIGHT

    def update(self):
        self.rect.y += self.vel_y
        self.rect.x += self.vel_x
        
    def apply_gravity(self):
        if self.jumping == True:
            self.vel_y += 0.2
            if self.rect.y > GROUND:
                self.jumping = False
                self.vel_y = 0
                self.rect.y = GROUND

        if self.rect.y < GROUND:
            self.rect.y += 2

    def move_right(self):
        self.rect.x += self.speed
        self.facing = RIGHT

    def move_left(self):
        self.rect.x -= self.speed
        self.facing = LEFT

    def jump(self):
        if self.stamina > 100 and self.jumping == False:
            self.stamina -= 100
            self.vel_y = -self.jump_speed
            self.jumping = True
