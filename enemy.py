from settings import *
import pygame
from map import Map
import math

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 32
        self.speed = 2
        self.health = 100
        self.radius = 5
        self.alive = True
        self.sprite = pygame.image.load('sprites/enemy.png').convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (64, 64))
        self.distance_to_player = 0
        self.angle_to_player = 0
        self.visible = False
    
    def update(self, player):
        if not self.alive:
            return

        dx = player.x - self.x
        dy = player.y - self.y
        self.distance_to_player = math.sqrt(dx**2 + dy**2)
        self.angle_to_player = math.atan2(dy, dx)
        
        if self.distance_to_player > 50:
            new_x = self.x + math.cos(self.angle_to_player) * self.speed
            new_y = self.y + math.sin(self.angle_to_player) * self.speed
            
            if not Map().is_wall(new_x, self.y):
                self.x = new_x
            if not Map().is_wall(self.x, new_y):
                self.y = new_y
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.alive = False
    
    def render_minimap(self, screen):
        if self.alive:
            pygame.draw.circle(screen, (120, 20, 30), (self.x // 4, self.y // 4), self)