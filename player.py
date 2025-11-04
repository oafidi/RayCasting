import pygame
from settings import *
from map import Map
import math

class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.radius = 5
        self.angle = 180 * (PI / 180)
        self.turnDirection = 0
        self.walkDirection = 0
        self.moveSpeed = 15
        self.rotationSpeed = 4 * (PI / 180)

    def update(self):
        keys = pygame.key.get_pressed()

        self.turnDirection = 0
        self.walkDirection = 0
        if keys[pygame.K_LEFT]:
            self.turnDirection = -1
        if keys[pygame.K_RIGHT]:
            self.turnDirection = 1
        if keys[pygame.K_UP]:
            self.walkDirection = 1
        if keys[pygame.K_DOWN]:
            self.walkDirection = -1
        self.angle += self.turnDirection * self.rotationSpeed
        moveStep = self.walkDirection * self.moveSpeed
        newX = self.x + math.cos(self.angle) * moveStep
        newY = self.y + math.sin(self.angle) * moveStep
        if not Map().is_wall(newX, newY):
            self.x = newX
            self.y = newY
    
    def render(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x // 4, self.y // 4), self.radius)
