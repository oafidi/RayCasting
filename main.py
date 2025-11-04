import pygame
from settings import *
from map import Map
from player import Player
from raycaster import Raycaster
from enemy_manager import EnemyManager

screen = pygame.display.set_mode((WIDTH, HEIGHT))

map = Map()
player = Player()
ray_caster = Raycaster(player)
enemy_manager = EnemyManager()

enemy_manager.add_enemy(500, 200)
enemy_manager.add_enemy(400, 90)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((0, 0, 0))
    enemy_manager.update(player)
    #pygame.draw.rect(screen, map.ceilling, (0, 0, WIDTH, HEIGHT // 2))
    #pygame.draw.rect(screen, map.floor, (0, HEIGHT // 2, WIDTH, HEIGHT // 2))
    player.update()
    ray_caster.cast_rays()
    map.render(screen)
    ray_caster.render(screen)
    enemy_manager.render_sprites(screen, player, ray_caster)
    player.render(screen)
    pygame.display.flip()
