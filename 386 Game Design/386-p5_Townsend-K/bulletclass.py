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


class BulletUp(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([4, 4])
        self.image.fill(BLACK)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        self.rect.y -= 3
        
class BulletDown(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([4, 4])
        self.image.fill(BLACK)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        self.rect.y += 3
        
class BulletLeft(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([4, 4])
        self.image.fill(BLACK)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        self.rect.x -= 3
        
class BulletRight(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([4, 4])
        self.image.fill(BLACK)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        self.rect.x += 3         

class EnemyBulletRight(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([4, 4])
        self.image.fill(BLUE)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        self.rect.x += 3 


class EnemyBulletLeft(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([4, 4])
        self.image.fill(BLUE)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        self.rect.x -= 3
        
class EnemyBulletUp(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([4, 4])
        self.image.fill(BLUE)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        self.rect.y -= 3
        
class EnemyBulletDown(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([4, 4])
        self.image.fill(BLUE)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        self.rect.y += 3
