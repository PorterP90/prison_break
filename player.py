import pygame
import math




class playerClass(pygame.spirt.Sprite):
    def __init__(self, x, y):
        #create the player
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 50, 50)
        self.speed = 2
        

    def checkMovement(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.rect.x -= self.speed
        elif key[pygame.K_s]:
            self.rect.y += self.speed
        elif key[pygame.K_d]:
            self.rect.x += self.speed
        elif key[pygame.K_w]:
            self.rect.y -ß= self.speed

    def update(self):
        self.checkMovement
        
