import pygame
from player import playerClass


pygame.init()


#Create game window
screenHight, screenWidth = 500, 500
screenColor = (166, 247, 226)
screen = pygame.display.set_mode((screenWidth, screenHight))
screen.fill(screenColor)



#framerate
clock = pygame.time.Clock()
frameRate = 60

#game running
running = True


def gameLoop():

    

    gameLoops = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.K_ESCAPE:
                pygame.quit()
        
        
        
        pygame.display.update()

    return None


gameLoop()



