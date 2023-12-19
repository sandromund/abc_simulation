import random
import sys

import numpy as np
import pygame

window_size = 1000
pygame.init()
clock = pygame.time.Clock()
fps = 30


# TODO Refactoring and comments

def f(x, y) -> float:
    # Himmelblau's function
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

n = 100
# The ABC generates a randomly distributed initial population of SN solutions (food sources),
# where n denotes the swarm size
solutions = [(random.randint(0, window_size - 1), random.randint(0, window_size - 1)) for _ in range(n)]
dimension = 2  # x and y


def generate_new_candidate_solution(k):
    candidate_solution = []
    for i in range(dimension):
        o = random.uniform(-1, 1)
        j = random.randint(0, n - 1)
        while j == i:
            j = random.randint(0, n - 1)
        solutions_l = [solutions[k][i], solutions[j][i]]
        candidate_solution.append(round(solutions[k][i] + o * (max(solutions_l) - min(solutions_l))) % 1000)
    return candidate_solution


def fitness(solution):
    x, y = solution
    return bg[x][y][1]


save_frames = False
frame_count = 0

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

    # TODO Bees evaluates its nectar amount and dances in the hive

    pygame.surfarray.blit_array(screen, bg)
    for k in range(n):
        pygame.draw.circle(screen, (255, 255, 255), solutions[k], 3)
    pygame.display.update()

    if save_frames:
        frame_count += 1
        filename = "screen_%04d.png" % (frame_count)
        pygame.image.save(screen, filename)

    clock.tick(fps)

    if frame_count > fps * 10:
        break

pygame.quit()
sys.exit()
