from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_SHOOT_COOLDOWN, PLAYER_SHOOT_SPEED, PLAYER_TURN_SPEED, PLAYER_SPEED
import pygame


class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown_timer = 0


    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt    

    def shoot(self):
        shot = Shot(x=self.position.x, y=self.position.y)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED 
        self.shoot_cooldown_timer += PLAYER_SHOOT_COOLDOWN
        
    def update(self, dt):
        self.shoot_cooldown_timer -= dt
        if self.shoot_cooldown_timer < 0:
            self.shoot_cooldown_timer = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
    
        if keys[pygame.K_SPACE] and self.shoot_cooldown_timer <= 0:
            self.shoot()
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    
        