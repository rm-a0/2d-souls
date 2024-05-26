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
def handle_events(p, hp_flask):
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

    # Hold controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        p.move_right()
    if keys[pygame.K_a]:
        p.move_left()
    if keys[pygame.K_SPACE]:
        p.jump()
 
def main(): 
    # Screen setup (16:9 aspect ratio)
    screen = pygame.display.set_mode((SCREEN_WIDTH ,SCREEN_HEIGHT))
    pygame.display.set_caption('dev/2d-er')
    clock = pygame.time.Clock()

    # Create objects
    p = Player(100, GROUND)
    e = Enemy(SCREEN_WIDTH - 200, GROUND)
    w = Weapon(50, 50)
    p.equip_weapon(w)
    hp_flask = Flask('hp', 5, 100)
    # Create ui
    ico = Icon(20, 20)
    p_hp_bar = Bar(120, 20, p.hp, RED) 
    p_mana_bar = Bar(120, 50, p.mana, BLUE)
    p_stamina_bar = Bar(120, 80, p.stamina, GREEN)
    # Append all sprites 
    sprites = pygame.sprite.Group(p, e, ico, p_hp_bar, p_mana_bar, p_stamina_bar)

    # Game loop
    running = True 
    while running:
        # Handle keyboard input
        handle_events(p, hp_flask)

        p.apply_gravity()
        p.refill_stamina(1)
        p.update()

        # Update ui
        p_hp_bar.update(p.hp)
        p_mana_bar.update(p.mana)
        p_stamina_bar.update(p.stamina)

        # Clear and draw new frame
        screen.fill(BLACK)
        sprites.draw(screen)
        pygame.display.flip()

        clock.tick(FPS)

if __name__ == "__main__":
    main()
