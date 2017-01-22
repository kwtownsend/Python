"""
Game By Kndall Townsend
CWID: 894121409
Based off the game Binding of Isaac
"""

import pygame, random
from pygame.locals import *


RED = (255, 0, 0)

#player.sprite
class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """
    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.speed = 1
        self.x_speed = 0
        self.y_speed = 0
        self.shootdelay = 1000
        self.upshoot = False
        self.downshoot = False
        self.leftshoot = False
        self.rightshoot = False
