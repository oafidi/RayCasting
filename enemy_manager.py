import pygame
import math
from settings import *
from enemy import Enemy

class EnemyManager:
    def __init__(self):
        self.enemies = []
    
    def add_enemy(self, x, y):
        self.enemies.append(Enemy(x, y))
    
    def update(self, player):
        for enemy in self.enemies:
            enemy.update(player)
    
    def render_sprites(self, screen, player, raycaster):
        visible_enemies = []
        
        for enemy in self.enemies:
            if not enemy.alive:
                continue
            dx = enemy.x - player.x
            dy = enemy.y - player.y
            angle_to_enemy = math.atan2(dy, dx)
            
            angle_diff = angle_to_enemy - player.angle
            
            while angle_diff > math.pi:
                angle_diff -= 2 * math.pi
            while angle_diff < -math.pi:
                angle_diff += 2 * math.pi

            if abs(angle_diff) < FOV_ANGLE / 2 + 0.5:
                visible_enemies.append((enemy, angle_diff, enemy.distance_to_player))
        visible_enemies.sort(key=lambda e: e[2], reverse=True)
        
        for enemy, angle_diff, distance in visible_enemies:
            self.render_sprite(screen, enemy, angle_diff, distance, player, raycaster)
    
    def render_sprite(self, screen, enemy, angle_diff, distance, player, raycaster):
        sprite_screen_x = (angle_diff / FOV_ANGLE) * WIDTH + (WIDTH / 2)
        sprite_height = (TILESIZE / distance) * raycaster.distance_player_screen
        sprite_width = sprite_height
        sprite_y = (HEIGHT / 2) - (sprite_height / 2)
        sprite_x = sprite_screen_x - (sprite_width / 2)
        scaled_sprite = pygame.transform.scale(enemy.sprite, (int(sprite_width), int(sprite_height)))
        darkness = min(255, 60 / distance * 255)
        if darkness < 255:
            dark_surface = scaled_sprite.copy()
            dark_surface.fill((darkness, darkness, darkness), special_flags=pygame.BLEND_MULT)
            scaled_sprite = dark_surface

        screen.blit(scaled_sprite, (int(sprite_x), int(sprite_y)))

        if enemy.health < 100:
            health_bar_width = int(sprite_width * (enemy.health / 100))
            pygame.draw.rect(screen, (255, 0, 0), 
                           (int(sprite_x), int(sprite_y) - 10, int(sprite_width), 5))
            pygame.draw.rect(screen, (0, 255, 0), 
                           (int(sprite_x), int(sprite_y) - 10, health_bar_width, 5))
    
    def render_minimap(self, screen):
        for enemy in self.enemies:
            enemy.render_minimap(screen)
    
    def check_collision_with_player(self, player):
        for enemy in self.enemies:
            if not enemy.alive:
                continue
            if enemy.distance_to_player < 30:
                return True
        return False