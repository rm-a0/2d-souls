import pygame
from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 70))
        self.image.fill(GREEN)
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
        # Items
        self.equipped_weapon = None

    # Updates x and y position based on velocity
    def update(self):
        self.rect.y += self.vel_y
        self.rect.x += self.vel_x

    # Gravity implemented with ground as base 
    def apply_gravity(self):
        self.vel_y += GRAVITY
        # Reset jump flag veloctiy and y coord
        if self.rect.y > GROUND:
            self.vel_y = 0
            self.rect.y = GROUND
            self.jumping = False

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
        if self.stamina > JMP_S_COST and self.jumping == False: 
            self.stamina -= JMP_S_COST 
            self.vel_y = -self.jump_speed
            self.jumping = True

    # Increases x or y coordinate 
    def dash(self):
        if self.stamina > DASH_S_COST:
            self.stamina -= DASH_S_COST
            if self.facing == RIGHT:
                self.rect.x += DASH_DIST 
            if self.facing == LEFT:
                self.rect.x -= DASH_DIST 

    # Refills stamina by given amount
    def refill_stamina(self, amount):
        if self.stamina + amount <= PLAYER_MAX_STAMINA:
            self.stamina += amount

    # Passes weapon class reference
    def equip_weapon(self, weapon):
        self.equipped_weapon = weapon

    # Deals damage to object that is intersecting with weapon
    def attack(self, object):
        if self.stamina >= ATK_S_COST:
            self.stamina -= ATK_S_COST
            if self.facing == RIGHT:
                self.equipped_weapon.draw_weapon(self.rect.x + 50, self.rect.y + 35)
            else:
                self.equipped_weapon.draw_weapon(self.rect.x - self.equipped_weapon.length, self.rect.y + 35)
            if self.equipped_weapon.is_intersecting(object):
                damage = self.equipped_weapon.damage
                object.take_damage(damage)
