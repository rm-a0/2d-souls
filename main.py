#!/usr/bin/env python3
import pygame
from constants import *
from objs.player import Player  # Player class
from ui.bars import *           # Bar classes

def main(): 
    # Screen setup (16:9 aspect ratio)
    screen = pygame.display.set_mode((SCREEN_WIDTH ,SCREEN_HEIGHT))
    pygame.display.set_caption('dev/2d-er')

    # Create objects
    p = Player(100, GROUND)
    # Create ui
    p_hp_bar = Bar(20, 20, p.hp, 'red')
    p_mana_bar = Bar(20, 50, p.mana, 'blue')
    p_stamina_bar = Bar(20, 80, p.stamina, 'green')
    # Append sprites
    sprites = pygame.sprite.Group(p, p_hp_bar, p_mana_bar, p_stamina_bar)

    # Game loop
    running = True 
    while running: 
        for event in pygame.event.get(): 
            # Quit game
            if event.type == pygame.QUIT: 
                running = False

            # Press controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    p.jump()
        
        # Hold controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            p.move_right()
        if keys[pygame.K_a]:
            p.move_left()
        
        # Apply physics
        p.apply_gravity()
        # Update objects
        p.update()
        # Update ui
        p_hp_bar.update(p.hp)
        p_mana_bar.update(p.mana)
        p_stamina_bar.update(p.stamina)

        # Clear and draw new frame
        screen.fill('black')
        sprites.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()