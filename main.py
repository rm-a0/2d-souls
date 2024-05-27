#!/usr/bin/env python3
import pygame
import sys

from constants import *             # Constant variables
from objs.player import Player      # Player class
from objs.enemy import Enemy        # Enemy class
from objs.consumable import Flask   # Flask class
from objs.weapon import Weapon      # Weapon class
from ui.bars import Bar             # Bar classes
from ui.icons import Icon           # Icon class
from ui.slots import Slot           # Slot class

# Hanlde keyboard input
def handle_events(p, e, s1, hp_flask):
    for event in pygame.event.get():
        # Quit 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Press controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT:
                p.dash()
            elif event.key == pygame.K_e:
                hp_flask.refill_stat(p)
                s1.update_count()
        # Mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                p.attack(e)

    # Hold controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        p.move_right()
    if keys[pygame.K_a]:
        p.move_left()
    if keys[pygame.K_SPACE]:
        p.jump()

# Main 
def main():
    # Init important components
    pygame.init()
    pygame.font.init()

    # Screen setup (16:9 aspect ratio)
    screen = pygame.display.set_mode((SCREEN_WIDTH ,SCREEN_HEIGHT))
    pygame.display.set_caption('dev/2d-souls')
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 26)

    # Create objects
    p = Player(100, GROUND)
    e = Enemy(SCREEN_WIDTH - 200, GROUND)
    w = Weapon(WEAPON_DAMAGE, WEAPON_WEIGHT, WEAPON_LENGTH, WEAPON_WIDTH)
    p.equip_weapon(w)
    hp_flask = Flask('hp', 5, 100)

    # Create ui
    ico = Icon(20, 20)
    p_hp_bar = Bar(120, 20, p.hp, RED)
    p_mana_bar = Bar(120, 50, p.mana, BLUE)
    p_stamina_bar = Bar(120, 80, p.stamina, GREEN)
    e_hp_bar = Bar(200, SCREEN_HEIGHT - 50, e.hp, RED)
    s1 = Slot(20, GROUND + 20, font)
    s1.switch_item(hp_flask)
    s1.update_count()

    # Append all sprites 
    sprites = pygame.sprite.Group(p, e, w, ico, p_hp_bar, p_mana_bar, p_stamina_bar, e_hp_bar, s1)

    # Game loop
    running = True 
    while running:
        # Handle keyboard input
        handle_events(p, e, s1, hp_flask)

        p.apply_gravity()
        p.refill_stamina(1)
        p.update()

        # Update ui
        p_hp_bar.update(p.hp)
        p_mana_bar.update(p.mana)
        p_stamina_bar.update(p.stamina)
        if e.hp > 0: 
            e_hp_bar.update(e.hp)

        # Clear and draw new frame
        screen.fill(BLACK)
        sprites.draw(screen)
        pygame.display.flip()

        clock.tick(FPS)

if __name__ == "__main__":
    main()
