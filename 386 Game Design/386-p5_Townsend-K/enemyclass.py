"""
Game By Kndall Townsend
CWID: 894121409
Based off the game Binding of Isaac
"""

import pygame, random
from pygame.locals import *

class Block(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([20, 15])
        self.image.fill(color)
        self.enemyshootdelay = 100

        self.rect = self.image.get_rect()
        #make ai not go in circles
        self.direction = "none"
        self.speedmultiplier = 1
        directionrng = random.randint(0,3)
        if self.direction == "none":
            if directionrng == 0:
                self.direction = "left"
            elif directionrng == 1:
                self.direction = "right"
            elif directionrng == 2:
                self.direction = "up"
            elif directionrng == 3:
                self.direction = "down"
        randomdirection = random.randint(0,1)
        if randomdirection == 0:
            self.x_speed = 1
        if randomdirection == 1:
            self.x_speed = -1

        randomdirection = random.randint(0,1)            
        if randomdirection == 0:
            self.y_speed = 1
        if randomdirection == 1:
            self.y_speed = -1
