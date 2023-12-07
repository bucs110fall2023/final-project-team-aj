import pygame

# Model
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, length):
        super().__init__()
        self.length = length
        # Surface -> Rectangles
        self.image = pygame.surface.Surface([self.length, self.length])
        self.image.fill("white")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y