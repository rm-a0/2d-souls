import pygame
from constants import *
from objs.entity import Entity

class Player(Entity):
    def __init__(self, x, y, width, height, color, hp, speed, mana, stamina, jspeed):
        super().__init__(x, y, width, height, color, hp, speed)
        # Additional stats
        self.max_stamina = stamina
        self.stamina = stamina
        self.max_mana = mana 
        self.mana = mana 
        self.jump_speed = jspeed
        # Flags
        self.jumping = False
        self.facing = RIGHT
        self.deflect_duration = 0 
        self.stop_duration = 0

    # Updates x and y position based on velocity
    # Decrements stop duration every game cycle
    def update(self):
        if self.stop_duration > 0:
            self.stop_duration -= 1
        if self.deflect_duration > 0:
            self.deflect_duration -= 1
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
        if self.stop_duration <= 0:
            self.rect.x += self.speed
            self.facing = RIGHT

    # Decreases x coordinate
    def move_left(self):
        if self.stop_duration <= 0:
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

    # Deals damage to object that is intersecting with weapon
    def attack(self, obj):
        if self.stamina >= ATK_S_COST:
            self.stamina -= ATK_S_COST
            self.stop_duration = 9
            if self.facing == RIGHT:
                self.weapon.draw_weapon(self.rect.x + PLAYER_WIDTH, self.rect.y + PLAYER_HEIGHT/2)
            else:
                self.weapon.draw_weapon(self.rect.x - self.weapon.length, self.rect.y + PLAYER_HEIGHT/2)
            if self.weapon.is_intersecting(obj):
                self.weapon.deal_damage(obj)

    # Deflects enemy attack
    def counter(self):
        if self.stamina >= CTR_S_COST:
            self.stamina -= CTR_S_COST
            self.stop_duration = CTR_DURATION
            self.deflect_duration = CTR_DURATION 
