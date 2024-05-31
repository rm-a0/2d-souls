#!/usr/bin/env python3
import pygame
import sys

from core.const import *                # Constant variables
from core.settings import *                 # Settings

from utils.calc import *                    # Import utilities for calculating

from objs.obj_factory import ObjFactory     # Object factory class
from objs.player import Player              # Player class
from objs.enemy import Enemy                # Enemy class
from objs.consumable import Flask           # Flask class
from objs.weapon import Weapon              # Weapon class

from ui.ui_factory import UiFactory         # Ui factory class
from ui.bars import Bar                     # Bar classes
from ui.icons import Icon                   # Icon class
from ui.slots import Slot                   # Slot class

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
    p = ObjFactory.create_player()
    e = ObjFactory.create_enemy()
    w1 = ObjFactory.create_weapon()
    w2 = ObjFactory.create_weapon()
    p.equip_weapon(w1)
    e.equip_weapon(w2)
    hp_flask = ObjFactory.create_hp_flask(5)
    mana_flask = ObjFactory.create_mana_flask(2)

    # Create UI
    ico = UiFactory.create_main_icon() 
    p_hp_bar = UiFactory.create_player_hp_bar(p)
    p_mana_bar = UiFactory.create_player_mana_bar(p)
    p_stamina_bar = UiFactory.create_player_stamina_bar(p)
    e_hp_bar = UiFactory.create_boss_hp_bar(e)
    s1 = UiFactory.create_slot_1(font)
    s1.switch_item(hp_flask)
    s1.update_count()
    s2 = UiFactory.create_slot_2(font)
    s2.switch_item(mana_flask)
    s2.update_count()

    # Append all sprites 
    sprites = pygame.sprite.Group(p, e, w1, w2, ico, p_hp_bar, p_mana_bar, p_stamina_bar, e_hp_bar, s1, s2)

    # Game loop
    running = True 
    while running:
        # Handle keyboard input
        handle_input(p, e, s1, s2)

        # Calculate distance
        dist = calc_dist(p.rect.center, e.rect.center)
        direction = calc_dir(p.rect.x, e.rect.x)

        # Handle player
        p.apply_gravity()
        p.refill_stamina(1)
        p.update()

        # Handle enemy
        e.update(dist)
        e.perform_action(direction, p)

        # Update ui
        if p.hp > 0:
            p_hp_bar.update(p.hp)
            p_mana_bar.update(p.mana)
            p_stamina_bar.update(p.stamina)
        else:
            print("You lost")
            break
        if e.hp > 0: 
            e_hp_bar.update(e.hp)
        else:
            print("You won")
            break

        # Clear and draw new frame
        screen.fill(BLACK)
        sprites.draw(screen)
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
