#!/usr/bin/env python3
import pygame
  
# Screen setup (16:9 aspect ratio)
screen = pygame.display.set_mode((1366 ,768))
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