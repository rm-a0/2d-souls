#!/usr/bin/env python3
import pygame
from constants import *
  
# Screen setup (16:9 aspect ratio)
screen = pygame.display.set_mode((SCREEN_WIDTH ,SCREEN_HEIGHT))
pygame.display.set_caption('beta') 
screen.fill('black')
  
# Update the display using flip 
pygame.display.flip() 
  
running = True 
while running:    
    for event in pygame.event.get(): 
        # QUIT event      
        if event.type == pygame.QUIT: 
            running = False