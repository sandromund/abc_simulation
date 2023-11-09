import pygame
import random


class Hive(pygame.sprite.Sprite):

    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.color = (255, 255, 0)
        self.position = (screen.get_width() // 2, screen.get_height() // 2)
        self.size = 30

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.position, self.size)


class Flower(pygame.sprite.Sprite):

    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.nectar = random.randint(100, 255)
        self.color = (self.nectar, 0, 0)
        self.position = (random.randint(0, screen.get_width()),
                         random.randint(0, screen.get_height()))
        self.size = 10

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.position, self.size)


class Bee(pygame.sprite.Sprite):

    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.color = (200, 100, 0)
        self.solution = (random.randint(0, screen.get_width()),
                         random.randint(0, screen.get_height()))
        self.dimension = len(self.solution)
        self.size = 3


    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.position, self.size)

    def generate_new_candidate_solution(self):
        v = candidate_solution = []
        for d in range(self.dimension):
            o = random.uniform(-1, 1)
            v.append(self.solution[d] + 0 )
