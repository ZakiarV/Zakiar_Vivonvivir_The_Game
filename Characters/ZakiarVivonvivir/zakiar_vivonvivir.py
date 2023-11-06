import pygame


class ZakiarVivonvivir(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.pos = pos
        self.image = pygame.Surface((32, 64))
        self.image.fill('green')
        self.rect = self.image.get_rect(center=self.pos)

        self.direction = pygame.math.Vector2()
        self.position = pygame.math.Vector2(self.pos)
        self.speed = 500

    def input(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w]:
            self.direction.y = -1
        elif keys_pressed[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys_pressed[pygame.K_a]:
            self.direction.x = -1
        elif keys_pressed[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        self.position.y += self.direction.y * self.speed * dt
        self.rect.centery = round(self.position.y)

        self.position.x += self.direction.x * self.speed * dt
        self.rect.centerx = round(self.position.x)

    def update(self, dt):
        self.input()
        self.move(dt)
