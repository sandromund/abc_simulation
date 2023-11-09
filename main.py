import math

import pygame
import sys
from math import sin
from src.hive import Hive, Flower
import numpy as np

window_size = 1000
pygame.init()


def f(x, y) -> float:
    return (x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2


def g(x, y):
    # range 0 , 1000
    x -= 500
    y -= 500
    # range -500 , 500
    x /= 100
    y /= 100
    # range -5 ,  5
    return x, y



def create_map(points):
    # sin(x)**2 + sin(y)  - sin(y)**2 - sin(x)
    bg = np.full((points, points, 3), 0, dtype=float)
    for x in range(points):
        for y in range(points):
            k =  f(*g(x, y))
            bg[x, y, 1] = k
    bg = bg / np.max(bg)
    bg = bg * 255
    return bg


screen = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption("ABC Sim")

n_flowers = 25
n_bees = n_flowers
h = Hive(screen)
flowers = [Flower(screen) for _ in range(n_flowers)]
bees = [Flower(screen) for _ in range(n_bees)]
bg = create_map(window_size)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    h.draw()
    [f.draw() for f in flowers + bees]
    # pygame.display.flip()
    pygame.surfarray.blit_array(screen, bg)
    pygame.display.update()
pygame.quit()
sys.exit()
