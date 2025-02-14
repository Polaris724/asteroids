import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position,self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        old_radius = self.radius
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_velocity1 = (self.velocity.rotate(random.uniform(20, 50))) * 1.2
            new_velocity2 = (self.velocity.rotate(-random.uniform(20, 50))) * 1.2
            self.radius = old_radius -  ASTEROID_MIN_RADIUS
            new_astoroid1 = Asteroid(self.position.x, self.position.y, self.radius)
            new_astoroid1.velocity = new_velocity1
            new_astoroid2 = Asteroid(self.position.x, self.position.y, self.radius)
            new_astoroid2.velocity = new_velocity2

