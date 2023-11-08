import pygame
import sys

from src.hive import Hive, Flower

window_size = 1000
pygame.init()
background_color = (0, 0, 0)



screen = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption("ABC Sim")

n_flowers = 25
n_bees = n_flowers
h = Hive(screen)
flowers = [Flower(screen) for _ in range(n_flowers)]
bees = [Flower(screen) for _ in range(n_bees)]


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(background_color)
    h.draw()
    [f.draw() for f in flowers + bees]
    pygame.display.flip()
pygame.quit()
sys.exit()
