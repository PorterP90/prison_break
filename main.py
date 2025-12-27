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
frameRate = 120

#game running
running = True


def gameLoop():

    

    gameLoops = 0
    running = True

    guards = pygame.sprite.Group()

    player = playerClass(screenHight//2, screenWidth//2, screenHight, screenWidth)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == pygame.K_ESCAPE:
                pygame.quit()
        

        player.update()
        screen.fill(screenColor)
        pygame.draw.rect(screen, (255,0,0), player.rect)
        

        pygame.display.update()



        gameLoops += 1
        clock.tick(frameRate)

    return None


gameLoop()



