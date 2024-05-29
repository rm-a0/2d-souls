import pygame
from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
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
        self.deflect_duration = 0 
        self.stop_duration = 0
        # Items
        self.equipped_weapon = None

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

    # Passes weapon class reference
    def equip_weapon(self, weapon):
        self.equipped_weapon = weapon

    # Decreases hp by given amount
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.kill()

    # Deals damage to object that is intersecting with weapon
    def attack(self, obj):
        if self.stamina >= ATK_S_COST:
            self.stamina -= ATK_S_COST
            self.stop_duration = 9
            if self.facing == RIGHT:
                self.equipped_weapon.draw_weapon(self.rect.x + PLAYER_WIDTH, self.rect.y + PLAYER_HEIGHT/2)
            else:
                self.equipped_weapon.draw_weapon(self.rect.x - self.equipped_weapon.length, self.rect.y + PLAYER_HEIGHT/2)
            if self.equipped_weapon.is_intersecting(obj):
                damage = self.equipped_weapon.damage
                obj.take_damage(damage)

    # Deflects enemy attack
    def counter(self):
        if self.stamina >= CTR_S_COST:
            self.stamina -= CTR_S_COST
            self.stop_duration = CTR_DURATION
            self.deflect_duration = CTR_DURATION 
