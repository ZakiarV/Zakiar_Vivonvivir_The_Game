import pygame
from Characters.ZakiarVivonvivir.zakiar_vivonvivir import ZakiarVivonvivir


class LevelGeneration:
    def __init__(self):
        self.display_screen = pygame.display.get_surface()

        self.player_sprite = pygame.sprite.GroupSingle()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()

        self.setup()

    def setup(self):
        self.zakiar_vivonvivir = ZakiarVivonvivir((600, 375), self.player_sprite)

    def update(self, dt):
        self.player_sprite.update(dt)
        self.player_sprite.draw(self.display_screen)
