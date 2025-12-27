import pygame
import math




class playerClass(pygame.sprite.Sprite):
    def __init__(self, x, y, screenHight, screenWidth):
        #create the player
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 25, 25)
        self.speed = 2
        self.screenHight = screenHight
        self.screenWidth = screenWidth
        self.activeSlot = None
        self.itemSlot1 = None
        self.itemSlot2 = None
        self.itemSlot3 = None
        self.itemSlot4 = None
        

    def checkMovement(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.rect.x -= self.speed
        if key[pygame.K_s]:
            self.rect.y += self.speed
        if key[pygame.K_d]:
            self.rect.x += self.speed
        if key[pygame.K_w]:
            self.rect.y -= self.speed
    
    def outOfBounds(self, screenHight, screenWidth):
        if self.rect.right >= screenWidth:
            self.rect.right = screenWidth
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screenHight:
            self.rect.bottom = screenHight
    
    def switchSlot(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_1] and self.itemSlot1 != None:
            self.activeSlot = self.itemSlot1
        elif key[pygame.K_2] and self.itemSlot2 != None:
            self.activeSlot = self.itemSlot2
        elif key[pygame.K_3] and self.itemSlot3 != None:
            self.activeSlot = self.itemSlot3
        elif key[pygame.K_4] and self.itemSlot4 != None:
            self.activeSlot = self.itemSlot4

    def update(self):
        self.checkMovement()
        self.outOfBounds(self.screenHight, self.screenWidth)
        self.switchSlot()
        
