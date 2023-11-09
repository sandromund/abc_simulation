import math

import pygame
import sys
from src.hive import Hive, Bee
import numpy as np
import random

window_size = 1000
pygame.init()
clock = pygame.time.Clock()
fps = 30


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
    bg = np.full((points, points, 3), 0, dtype=float)
    for x in range(points):
        for y in range(points):
            k = f(*g(x, y))
            bg[x, y, 1] = k
    bg = bg / np.max(bg)
    bg = bg * 255
    return bg


screen = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption("ABC Sim")
bg = create_map(window_size)

n = 10000
# The ABC generates a randomly distributed initial population of SN solutions (food sources),
# where SN denotes the swarm size
solutions = [(random.randint(0, window_size-1), random.randint(0, window_size-1)) for _ in range(n)]
dimension = 2  # x and y


def generate_new_candidate_solution(k):
    candidate_solution = []
    for i in range(dimension):
        o = random.uniform(-1, 1)
        j = random.randint(0, n - 1)
        while j == i:
            j = random.randint(0, n - 1)
        l = [solutions[k][i], solutions[j][i]]
        candidate_solution.append(round(solutions[k][i] + o * (max(l) - min(l))) % 1000)
    return candidate_solution


def fitness(solution):
    x, y = solution
    return bg[x][y][1]


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Each employed bee goes to a food source in her memory and determines a closest source
    for k in range(n):
        c = generate_new_candidate_solution(k)
        if fitness(c) < fitness(solutions[k]):
            solutions[k] = c



    # #then evaluates its nectar amount and dances in the hive

    # pygame.display.flip()
    pygame.surfarray.blit_array(screen, bg)

    for k in range(n):
        pygame.draw.circle(screen, (255, 255, 255), solutions[k], 3)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
sys.exit()
