import pygame
import math
import random 
from items import *


class guardClass(pygame.sprite.Spirte):
    def __init__(self, screenHight, screenWidth):
        x = random.randint(0,screenHight)
        y = random.randint(0,screenWidth)
        #create a guard
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 25, 25)
        self.speed = 1 
        self.weapon1 = None
        self.weapon2 = None

class guardLevel1(guardClass):
    def __init__(self):
        self.speed = 2
        self.weapon1 = baton
        self.weapon2 = tazer

class guardLevel2(guardClass):
    def __init__(self):
        self.speed = 1
        self.weapon1 = glock20
        self.weapon2 = baton
