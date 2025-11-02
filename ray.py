from settings import *
import pygame
from map import Map
import math

def normalize_angle(angle):
    return angle % (2 * math.pi)

def distance_between_points(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

class Ray:
    def __init__(self, player, ray_angle):
        self.ray_angle = normalize_angle(ray_angle)
        self.player = player
        self.wall_hit_x = 0
        self.wall_hit_y = 0
        self.distance = 0
        self.is_facing_down = self.ray_angle > 0 and self.ray_angle < math.pi
        self.is_facing_up = not self.is_facing_down
        self.is_facing_right = self.ray_angle < 0.5 * math.pi or self.ray_angle > 1.5 * math.pi
        self.is_facing_left = not self.is_facing_right

    def cast(self):
        found_horz_wall_hit = False
        horizontal_wall_hit_x = 0
        horizontal_wall_hit_y = 0

        # Horizontal Intersection
        first_intersection_y = math.floor(self.player.y / TILESIZE) * TILESIZE
        if self.is_facing_down:
            first_intersection_y += TILESIZE
            
        first_intersection_x = self.player.x + (first_intersection_y - self.player.y) / math.tan(self.ray_angle)
        
        next_horz_touch_x = first_intersection_x
        next_horz_touch_y = first_intersection_y

        ya = TILESIZE if self.is_facing_down else -TILESIZE
        xa = ya / math.tan(self.ray_angle) if math.tan(self.ray_angle) != 0 else 0

        while (0 <= next_horz_touch_x <= WIDTH and 0 <= next_horz_touch_y <= HEIGHT):
            check_y = next_horz_touch_y - 1 if self.is_facing_up else next_horz_touch_y
            
            if Map().is_wall(next_horz_touch_x, check_y):
                horizontal_wall_hit_x = next_horz_touch_x
                horizontal_wall_hit_y = next_horz_touch_y
                found_horz_wall_hit = True
                break
            else:
                next_horz_touch_x += xa
                next_horz_touch_y += ya
        
        # Vertical Intersection
        found_vert_wall_hit = False
        vertical_wall_hit_x = 0
        vertical_wall_hit_y = 0
        
        first_intersection_x = math.floor(self.player.x / TILESIZE) * TILESIZE
        if self.is_facing_right:
            first_intersection_x += TILESIZE
            
        first_intersection_y = self.player.y + (first_intersection_x - self.player.x) * math.tan(self.ray_angle)
        
        next_vert_touch_x = first_intersection_x
        next_vert_touch_y = first_intersection_y


        xb = TILESIZE if self.is_facing_right else -TILESIZE
        yb = xb * math.tan(self.ray_angle)

        while (0 <= next_vert_touch_x <= WIDTH and 0 <= next_vert_touch_y <= HEIGHT):
            check_x = next_vert_touch_x - 1 if self.is_facing_left else next_vert_touch_x
            
            if Map().is_wall(check_x, next_vert_touch_y):
                vertical_wall_hit_x = next_vert_touch_x
                vertical_wall_hit_y = next_vert_touch_y
                found_vert_wall_hit = True
                break
            else:
                next_vert_touch_x += xb
                next_vert_touch_y += yb

        horz_distance = distance_between_points(self.player.x, self.player.y, 
                                                horizontal_wall_hit_x, horizontal_wall_hit_y) if found_horz_wall_hit else float('inf')
        vert_distance = distance_between_points(self.player.x, self.player.y, 
                                               vertical_wall_hit_x, vertical_wall_hit_y) if found_vert_wall_hit else float('inf')
        
        if vert_distance < horz_distance:
            self.wall_hit_x = vertical_wall_hit_x
            self.wall_hit_y = vertical_wall_hit_y
            self.distance = vert_distance
        else:
            self.wall_hit_x = horizontal_wall_hit_x
            self.wall_hit_y = horizontal_wall_hit_y
            self.distance = horz_distance

    def render(self, screen):
        pygame.draw.line(screen, (255, 0, 0), (self.player.x, self.player.y),
                        (self.wall_hit_x, self.wall_hit_y), 3)