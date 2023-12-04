import pygame
from src.screens import Screens

class Paddle(Screens):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.xpos = self.starting_xpos = x
        self.ypos = self.starting_ypos = y
        self.width = width
        self.height = height
        pygame.draw.rect(self.screen, "white", (self.xpos, self.ypos), self.width, self.height)
        
    def move(self):
        self.paddle_vel = 4
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.xpos += self.paddle_vel
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.xpos -= self.paddle_vel
    
    def reset(self):
        self.x = self.starting_xpos
        self.y = self.starting_ypos