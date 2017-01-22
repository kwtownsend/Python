"""
Game By Kndall Townsend
CWID: 894121409
Based off the game Binding of Isaac
"""

import pygame, random
from pygame.locals import *


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIME = (0, 255, 0)
red = (200,0,0)
PINK = (255, 102, 255)

class Powerup(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([20, 15])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()  
