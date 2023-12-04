import pygame
from src.screens import Screens
from src.ball import Ball
from src.paddle import Paddle

class Controller:
    
    def __init__(self, up_score, down_score):
        pygame.init()
        self.s = Screens()
        self.ball = Ball()
        self.paddle = Paddle()
        self.up_score = up_score
        self.down_score = down_score
        
    def score(self):
        font = pygame.font.Font(None, 48)
        self.up_score_text = font.render(f"{self.up_score}", True, "white")
        self.down_score_text = font.render(f"{self.down_score}", True, "white")
        self.s.screen.blit(self.up_score_text, (self.s.window_width - 10, self.s.window_height/2 - 10))
        self.s.screen.blit(self.down_score_text, (self.s.window_width - 10, self.s.window_height/2 + 10))
    
    def collision(self):
        if self.ball.xpos - self.ball.radius == 0:
            self.ball.x_vel *= -1
        elif self.ball.xpos + self.ball.radius == self.s.window_width:
            self.ball.x_vel *= -1
            
        if self.ball.y_vel < 0:
            if self.ball.xpos - self.ball.radius <= self.paddle.xpos + self.paddle.height and self.ball.xpos + self.ball.radius >= self.paddle.xpos + self.paddle.height:
                if self.ball.ypos + self.ball.radius == self.paddle.ypos + self.paddle.width:
                    self.ball.y_vel *= -1
                    
                    self.center_paddle = (self.paddle.xpos + self.paddle.height) / 2
                    self.difference_x = self.center_paddle - self.ball.xpos
                    #LEFT OFF HERE
                
      
    def startscreenloop(self):
        self.s.startscreen()

    def gameloop(self):
        self.s.gamescreen()
        self.score()
        self.ball.move()
        self.ball.reset()
        self.paddle.move()
        self.paddle.reset()
        
    
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
    
    