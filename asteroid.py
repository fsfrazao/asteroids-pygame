from circleshape import CircleShape
from constants import ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            fragment_1_velocity = self.velocity.rotate(angle)
            fragment_2_velocity = self.velocity.rotate(-angle)
            fragment_radius = self.radius - ASTEROID_MIN_RADIUS

            fragment_1 = Asteroid(self.position.x, self.position.y, radius=fragment_radius)
            fragment_1.velocity = fragment_1_velocity * 1.2

            fragment_2 = Asteroid(self.position.x, self.position.y, radius=fragment_radius)
            fragment_2.velocity = fragment_2_velocity * 1.2





    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", center = self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
