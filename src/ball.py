import pygame

# Model
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__()
        self.starting_xpos = x
        self.starting_ypos = y
        self.radius = radius
        self.max_vel = 1
        self.x_vel = 0
        self.y_vel = 0
        # Surface -> Rectangles
        self.image = pygame.surface.Surface([self.radius, self.radius])
        self.image.fill("white")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

    def reset(self):
        self.rect.x = self.starting_xpos
        self.rect.y = self.starting_ypos
        self.y_vel = 0
        self.x_vel = 0
