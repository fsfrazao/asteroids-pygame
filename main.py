import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clk = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    
    player = Player(x = SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        

        for unit in updatables:
            unit.update(dt)
        for unit in drawables:
            unit.draw(screen)    
        # player.update(dt)
        # player.draw(screen)
        pygame.display.flip()

        dt = clk.tick(60)/1000

if __name__ == "__main__":
    main()