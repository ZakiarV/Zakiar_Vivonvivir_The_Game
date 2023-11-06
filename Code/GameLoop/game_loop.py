import pygame
from Code.LevelGeneration.level_generation import LevelGeneration


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 750))
        self.clock = pygame.time.Clock()
        self.level = LevelGeneration()

    def run(self):
        running = True
        while running:
            dt = self.clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((0, 0, 0))
            self.level.update(dt)
            pygame.display.flip()
            self.clock.tick(60)
