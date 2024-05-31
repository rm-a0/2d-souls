import pygame
import sys

from objs.player import Player              # Player class
from objs.enemy import Enemy                # Enemy class
from objs.consumable import Flask           # Flask class
from objs.weapon import Weapon              # Weapon class

# Hanlde keyboard input
def handle_input(player, enemy, slot1, slot2):
    for event in pygame.event.get():
        # Quit 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Press controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT:
                player.dash()
            elif event.key == pygame.K_e:
                slot1.item.refill_stat(player)
                slot1.update_count()
            elif event.key == pygame.K_q:
                slot2.item.refill_stat(player)
                slot2.update_count()

        # Mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player.attack(enemy)
            elif event.button == 3:
                player.counter()

    # Hold controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        player.move_right()
    if keys[pygame.K_a]:
        player.move_left()
    if keys[pygame.K_SPACE]:
        player.jump()


