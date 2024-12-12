import pygame
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clk = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots,updatables, drawables)

    player = Player(x = SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        

        for unit in updatables:
            unit.update(dt)

        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                print("Game over!!!")
                return


        for asteroid in asteroids:
            for shot in shots:
                if asteroid.is_colliding(shot):
                    asteroid.split()
                    shot.kill()
                # else:
                #     print("No collisions detected")
            
        for unit in drawables:
            unit.draw(screen)    
        # player.update(dt)
        # player.draw(screen)
        pygame.display.flip()

        dt = clk.tick(60)/1000

if __name__ == "__main__":
    main()