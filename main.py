#!/usr/bin/env python3
import pygame
from constants import *
from objs.player import Player  # Player class


def main(): 
    # Screen setup (16:9 aspect ratio)
    screen = pygame.display.set_mode((SCREEN_WIDTH ,SCREEN_HEIGHT))
    pygame.display.set_caption('dev/2d-er')

    # Create objects
    p = Player(100, SCREEN_HEIGHT-150)

    running = True 
    while running: 
        for event in pygame.event.get(): 
            # QUIT event
            if event.type == pygame.QUIT: 
                running = False

        # Clear and draw new frame
        screen.fill('black')
        screen.blit(p.image, p.rect)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()