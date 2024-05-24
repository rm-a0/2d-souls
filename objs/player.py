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
        self.max_hp = PLAYER_MAX_HP
        self.max_mana = PLAYER_MAX_MANA
        self.max_stamina = PLAYER_MAX_STAMINA
        self.hp = PLAYER_MAX_HP
        self.mana = PLAYER_MAX_MANA
        self.stamina = PLAYER_MAX_STAMINA
        self.speed = PLAYER_SPEED
        self.jump_speed = JUMP_SPEED
        # Flags
        self.jumping = False
        self.facing = RIGHT

    # Updates x and y position based on velocity
    def update(self):
        self.rect.y += self.vel_y
        self.rect.x += self.vel_x

    # Gravity implemented with ground as base 
    def apply_gravity(self):
        self.vel_y += GRAVITY
        # Reset jump flag veloctiy and y coord
        if self.rect.y > GROUND:
            self.jumping = False
            self.vel_y = 0
            self.rect.y = GROUND

    # Increases x coordinate
    def move_right(self):
        self.rect.x += self.speed
        self.facing = RIGHT

    # Decreases x coordinate
    def move_left(self):
        self.rect.x -= self.speed
        self.facing = LEFT

    # Sets flag and decreases y velocity
    def jump(self):
        if self.stamina > 100 and self.jumping == False: 
            self.stamina -= 100
            self.vel_y = -self.jump_speed
            self.jumping = True

    # Increases x or y coordinate 
    def dash(self):
        if self.stamina > 100:
            self.stamina -= 100
            if self.facing == RIGHT:
                self.rect.x += 200 
            if self.facing == LEFT:
                self.rect.x -= 200 

    # Refills stamina by given amount
    def refill_stamina(self, amount):
        if self.stamina + amount <= PLAYER_MAX_STAMINA:
            self.stamina += amount
