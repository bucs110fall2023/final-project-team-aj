import pygame


class Paddle(pygame.sprite.Sprite):
    def __init__(self, x=1, y=1, color="white", width=225, height=20):
        """
        Initialize the paddle with specified or default values.

        Parameters:
        - x (int): The initial x-coordinate of the paddle.
        - y (int): The initial y-coordinate of the paddle.
        - color (str): The color of the paddle.
        - width (int): The width of the paddle.
        - height (int): The height of the paddle.
        """
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
        """
        Move the paddle left or right based on the specified direction.

        Parameters:
        - dir (str): The direction in which to move the paddle ("left" or "right").
        """
        if dir == "right":
            self.rect.x += self.paddle_vel
        if dir == "left":
            self.rect.x -= self.paddle_vel

    def reset(self):
        """
        Reset the paddle to its initial position.
        """

        self.rect.x = self.starting_xpos
        self.rect.y = self.starting_ypos
