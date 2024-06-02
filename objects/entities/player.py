import pygame

from core.constants import *
from objects.entities.entity import Entity

class Player(Entity):
    def __init__(self, x, y, width, height, color, hp, speed, mana, stamina, jspeed):
        super().__init__(x, y, width, height, color, hp, speed)
        # Additional stats
        self.max_stamina = stamina
        self.stamina = stamina
        self.max_mana = mana 
        self.mana = mana 
        self.jump_speed = jspeed

    # Increases x coordinate
    def move_right(self):
        if self.stun <= 0:
            self.velocity.x += self.speed
            self.facing = RIGHT

    # Decreases x coordinate
    def move_left(self):
        if self.stun <= 0:
            self.velocity.x -= self.speed
            self.facing = LEFT

    # Sets flag and decreases y velocity
    def jump(self):
        if self.stamina > JMP_S_COST and self.state != JUMP:
            self.stamina -= JMP_S_COST 
            self.velocity.y = -self.jump_speed
            self.state = JUMP

    # Dash in the direction player is facing 
    def dash(self):
        if self.stamina > DASH_S_COST:
            self.dash_duration = 120
            self.stamina -= DASH_S_COST
            if self.facing == RIGHT:
                self.velocity.x = self.speed*4 
            if self.facing == LEFT:
                self.velocity.x = -self.speed*4

    # Refills stamina by given amount
    def refill_stamina(self, amount):
        if self.stamina + amount <= PLAYER_MAX_STAMINA:
            self.stamina += amount

    # Deals damage to object that is intersecting with weapon
    def attack(self, obj):
        if self.stamina >= ATK_S_COST:
            self.stamina -= ATK_S_COST
            self.stun = 9
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
            self.stun = CTR_DURATION
            self.deflect = CTR_DURATION 
