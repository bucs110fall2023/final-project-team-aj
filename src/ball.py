import pygame
from src.screens import Screens

class Ball(Screens):
    def __init__(self, x, y, radius):
        super().__init__()
        self.xpos = self.starting_xpos = x
        self.ypos = self.starting_ypos = y
        self.radius = radius
        self.x_vel = 5
        self.y_vel = 0
        pygame.draw.circle(self.screen, "white", (self.xpos, self.ypos), self.radius)
        
    def move(self):
        self.xpos += self.x_vel
        self.ypos += self.y_vel
        
    def reset(self):
        self.xpos = self.starting_xpos
        self.ypos = self.starting_ypos
        self.y_vel = 0
        self.x_vel *= -1