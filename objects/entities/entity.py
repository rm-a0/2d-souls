import pygame

from core.constants import ENEMY_WIDTH, ENEMY_HEIGHT, GRAVITY, RIGHT, IDLE

class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, hp, speed):
        super().__init__()
        self.image = pygame.Surface((ENEMY_WIDTH, ENEMY_HEIGHT))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        # Physiscs 
        self.velocity = pygame.math.Vector2(0, 0)
        # Stats
        self.max_hp = hp
        self.hp = hp
        self.speed = speed
        # Flags
        self.facing = RIGHT
        self.jumping = False
        self.deflect = 0
        self.stun = 0
        self.dash_duration = 0

    # Passes weapon reference
    def equip_weapon(self, weapon):
        self.weapon = weapon

    def update(self, tiles):
        if self.stun > 0:
            self.stun -= 1
            return
        if self.deflect > 0:
            self.deflect -= 1
        if self.dash_duration > 0:
            self.dash_duration -= 1

        self.apply_gravity()
        self.rect.x += self.velocity.x
        self.tile_collision(tiles, 'horizontal')
        self.rect.y += self.velocity.y
        self.tile_collision(tiles, 'vertical')

        if self.dash_duration <= 0:
            self.velocity.x = 0

    def tile_collision(self, tiles, direction):
        for tile in tiles:
            if self.rect.colliderect(tile.rect):
                if direction == 'horizontal':
                    if self.velocity.x > 0:
                        self.rect.right = tile.rect.left
                    elif self.velocity.x < 0:
                        self.rect.left = tile.rect.right
                elif direction == 'vertical':
                    if self.velocity.y > 0:
                        self.velocity.y = 0
                        self.rect.bottom = tile.rect.top
                        self.jumping = False
                    elif self.velocity.y < 0:
                        self.rect.top = tile.rect.bottom
                        self.velocity.y = 0

    def apply_gravity(self):
        self.velocity.y += GRAVITY



