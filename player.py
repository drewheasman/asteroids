from circleshape import CircleShape
from constants import PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED
from constants import PLAYER_RADIUS, PLAYER_SHOOT_COOLDOWN
from shot import Shot
import pygame


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(
            self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_j]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_l]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_i]:
            self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_k]:
            self.move(-dt)
        if keys[pygame.K_SPACE] or keys[pygame.K_f]:
            self.shoot()

        if self.timer > 0:
            self.timer -= dt

    def move(self, dt):
        rotated_position = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += rotated_position * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer > 0:
            return

        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(
            self.rotation) * PLAYER_SHOOT_SPEED

        self.timer = PLAYER_SHOOT_COOLDOWN
