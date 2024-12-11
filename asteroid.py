from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def __spawn_child(self, angle, radius):
        vector = self.velocity.rotate(angle)
        child = Asteroid(self.position.x, self.position.y, radius)
        child.velocity = vector * 1.2

    def hit(self):
        self.kill()

        if self.radius < ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        radius = self.radius - ASTEROID_MIN_RADIUS

        self.__spawn_child(angle, radius)
        self.__spawn_child(-angle, radius)
