import pygame
import math
import random 
from items import *


class guardClass(pygame.sprite.Sprite):
    def __init__(self, screenHight, screenWidth):
        x = random.randint(0,screenHight)
        y = random.randint(0,screenWidth)
        #create a guard
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 25, 25)
        self.speed = 1 
        self.weapon1 = None
        self.weapon2 = None
        self.followDistance = None

    

    def alertLevel(self, player, level):
        self.followDistance = random.randint(30//level, 45//level)
        playerXY = player.rect.center 
        CopXY = self.rect.center
        #I THINK THE PROBLEM HAS TO DO WITH THE LINE BELOW HERE FOR MY FOLLOW TECH
        if abs(playerXY[0] - CopXY[0]) > self.followDistance or abs(playerXY[1] - CopXY[1]) > self.followDistance:
            #this check find out if cop is outside follow distance
            dx = player.rect.center[0] - self.rect.center[0]
            dy = player.rect.center[1] - self.rect.center[1]

            dist = math.hypot(dx, dy)

            if dist != self.followDistance:
                dx /= dist
                dy /= dist

                moveX = dx * self.speed
                moveY = dy * self.speed

                self.rect.x += moveX
                self.rect.y += moveY


    def checkForSus(self, player):
        if player.susMeter >= 75:
            self.alertLevel(player, 3)
        if player.susMeter >= 50:
            self.alertLevel(player, 2)
        if player.susMeter >= 25:
            self.alertLevel(player, 1)


    def update(self, player):
        self.checkForSus(player)


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
