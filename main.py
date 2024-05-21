#!/usr/bin/env python3
import pygame
from constants import *
from objs.player import Player  # Player class

def main(): 
    # Screen setup (16:9 aspect ratio)
    screen = pygame.display.set_mode((SCREEN_WIDTH ,SCREEN_HEIGHT))
    pygame.display.set_caption('dev/2d-er') 
    screen.fill('black')

    # Update the display using flip 
    pygame.display.flip()

    # Create objects
    p = Player(200, 200)

    running = True 
    while running: 
        for event in pygame.event.get(): 
            # QUIT event
            if event.type == pygame.QUIT: 
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()