#!/usr/bin/env python3
import pygame
from constants import *
from objs.player import Player  # Player class

def main(): 
    # Screen setup (16:9 aspect ratio)
    screen = pygame.display.set_mode((SCREEN_WIDTH ,SCREEN_HEIGHT))
    pygame.display.set_caption('dev/2d-er')

    # Create objects
    p = Player(100, GROUND)
    sprites = pygame.sprite.Group(p)
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
        

        p.apply_gravity()
        p.update()

        # Clear and draw new frame
        screen.fill('black')
        sprites.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()