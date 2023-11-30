import pygame
from src.startscreen import Startscreen

class Controller:
    
    def __init__(self):
        pygame.init()
        self.window_width = 750
        self.window_height = 800
        self.screen = pygame.display.set_mode([self.window_width, self.window_height])
        self.state = "HOME"
        
    def score(self):
        self.score1 = 0
        self.score2 = 0
        #if ball collides with the bottom rectangle, score1 goes up by one
        #if ball collides with the top rectangle, score2 goes up by one
    
    def collision(self):
        pass
                
    def startscreenloop(self):
        s = Startscreen()
        s.startscreen()

    def gameloop(self):
        self.screen_color = (6, 168, 0)
        self.screen.fill(self.screen_color)
        goal_area1 = pygame.Rect(0, 0, self.window_width, 20)
        goal_area2 = pygame.Rect(0, self.window_height - 20, self.window_width, 20)
        pygame.draw.rect(self.screen, "white", goal_area1)
        pygame.draw.rect(self.screen, "white", goal_area2)
        pygame.draw.line(self.screen, "white", (0, self.window_height/2), (self.window_width, self.window_height/2), 2)
        pygame.display.flip()
    
    def endscreenloop(self):
        pass
    
    def mainloop(self):
        self.gameloop()
        # while self.state == "HOME":
        #     self.startscreenloop()
        #     for event in pygame.event.get():
        #         if event.type == pygame.MOUSEBUTTONDOWN:
        #             if self.starttext_hitbox.collidepoint(event.pos):
        #                 self.state = "GAME"
        # while self.state == "GAME":
        #     self.gameloop()
        
        #Exit the screen when user clicks out
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()
    
    