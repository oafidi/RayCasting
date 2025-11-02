import pygame
from settings import *
from ray import Ray
import math


class Raycaster:
    def __init__(self, player):
        self.player = player
        self.rays = []
        self.distance_player_screen = (WIDTH / 2) / math.tan(FOV_ANGLE / 2)

    def cast_rays(self):
        self.rays = []
        start_angle = self.player.angle - (FOV_ANGLE / 2)
        for ray_count in range(NUM_RAYS):
            ray_angle = start_angle + ray_count * (FOV_ANGLE / NUM_RAYS)
            ray = Ray(self.player, ray_angle)
            ray.cast()
            self.rays.append(ray)

    def render(self, screen):
        i = 0

        for ray in self.rays:
            #ray.render(screen)
            line_height = (TILESIZE / ray.distance) * self.distance_player_screen
            draw_start = int((HEIGHT / 2) - (line_height / 2))
            draw_end = line_height
            pygame.draw.rect(screen, (0, 255, 0), (i * RES, draw_start, RES, draw_end))
            i += 1