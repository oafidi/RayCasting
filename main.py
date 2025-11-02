import pygame
from settings import *
from map import Map
from player import Player
from raycaster import Raycaster

screen = pygame.display.set_mode((WIDTH, HEIGHT))

map = Map()
player = Player()
ray_caster = Raycaster(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((0, 0, 0))
    #map.render(screen)
    #player.render(screen)
    player.update()
    ray_caster.cast_rays()
    ray_caster.render(screen)
    pygame.display.flip()
