import pygame

# Model
class Obstacle(pygame.sprite.Sprite):
    """
    A class representing an obstacle in a game.

    Attributes:
    - width (int): The width of the obstacle.
    - height (int): The height of the obstacle.
    - image (pygame.Surface): The surface representing the visual appearance of the obstacle.
    - rect (pygame.Rect): The rectangle that defines the position and size of the obstacle.

    Methods:
    - __init__(self, x, y, width, height): Initializes a new Obstacle instance with the specified parameters.
    """
    def __init__(self, x, y, width, height):
        """
        Initializes a new Obstacle instance.

        Parameters:
        - x (int): The initial x-coordinate of the obstacle.
        - y (int): The initial y-coordinate of the obstacle.
        - width (int): The width of the obstacle.
        - height (int): The height of the obstacle.
        """
        super().__init__()
        self.width = width
        self.height = height
        # Surface -> Rectangles
        self.image = pygame.surface.Surface([self.width, self.height])
        self.image.fill("yellow")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y