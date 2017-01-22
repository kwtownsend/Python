"""
Game By Kndall Townsend
CWID: 894121409
Based off the game Binding of Isaac
"""

import pygame
from pygame.locals import *


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIME = (0, 255, 0)
red = (200,0,0)


#need multiple different kinds of barriers to make ai movement more dynamic or else they just hug the border
class HorizontalBarrier(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([50, 1])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()

class VerticalBarrier(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([1, 50])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()
class CenterVerticalBarrier(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([1, 200])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()
        
class CenterHorizontalBarrier(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([300, 1])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()


#border of game so things dont leave
class LeftRightBorder(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([1, 400])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()  

class TopBotBorder(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([700, 1])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()  
