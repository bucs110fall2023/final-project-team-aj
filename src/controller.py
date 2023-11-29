import pygame
# from ball import Ball

class Controller:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode()
        
    def score(self):
        pass
    
    def collision(self):
        pass
                
    def startscreenloop(self):
        self.screen_color = (6, 168, 0)
        self.screen.fill(self.screen_color)
        pygame.display.flip()

    def gameloop(self):
        pass
    
    def endscreenloop(self):
        pass
    
    def mainloop(self):
        self.startscreenloop()
        #Exit the screen when user clicks out
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()
    
    