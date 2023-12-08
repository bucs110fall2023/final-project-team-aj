import pygame


class Paddle(pygame.sprite.Sprite):
    def __init__(self, x=1, y=1, color="white", width=225, height=20):
        super().__init__()
        self.starting_xpos = x
        self.starting_ypos = y
        self.width = width
        self.height = height
        self.image = pygame.surface.Surface([self.width, self.height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.paddle_vel = 90

    def move(self, dir):
        if dir == "right":
            self.rect.x += self.paddle_vel
        if dir == "left":
            self.rect.x -= self.paddle_vel

    def reset(self):
        self.rect.x = self.starting_xpos
        self.rect.y = self.starting_ypos
