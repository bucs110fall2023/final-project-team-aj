import pygame
from src.screens import Screens
from src.ball import Ball
from src.paddle import Paddle

class Controller:
    
    def __init__(self, up_score=0, down_score=0):
        pygame.init()
        buffer = 10
        self.s = Screens()
        self.ball = Ball(self.s.window_width / 2, self.s.window_height / 2, 10)
        self.sample_paddle = Paddle()
        self.up_paddle = Paddle((self.s.window_width / 2) - self.sample_paddle.width, buffer)
        self.down_paddle = Paddle((self.s.window_width / 2) - self.sample_paddle.width, self.s.window_height - buffer - self.sample_paddle.height)
        self.up_score = up_score
        self.down_score = down_score
        
    def score(self):
        font = pygame.font.Font(None, 48)
        self.up_score_text = font.render(f"{self.up_score}", True, "white")
        self.down_score_text = font.render(f"{self.down_score}", True, "white")
        self.s.screen.blit(self.up_score_text, (5, self.s.window_height/4))
        self.s.screen.blit(self.down_score_text, (self.s.window_width - 20, 3*(self.s.window_height/4)))
    
    def collision(self):
        if self.ball.xpos - self.ball.radius == 0:
            self.ball.x_vel *= -1
        elif self.ball.xpos + self.ball.radius == self.s.window_width:
            self.ball.x_vel *= -1
            
        if self.ball.y_vel < 0:
            if self.ball.xpos + self.ball.radius >= self.up_paddle.xpos and self.ball.xpos - self.ball.radius <= self.up_paddle.xpos + self.up_paddle.width:
                if self.ball.ypos - self.ball.radius == self.up_paddle.ypos + self.up_paddle.height:
                    self.ball.y_vel *= -1
                    
                    self.center_up_paddle = (self.up_paddle.xpos + self.up_paddle.width) / 2
                    self.difference_x = self.center_up_paddle - self.ball.xpos
                    self.reduction = (self.up_paddle.width / 2) / self.ball.max_vel
                    self.ball.x_vel = self.difference_x / self.reduction
                    
        else:
            if self.ball.xpos + self.ball.radius >= self.down_paddle.xpos and self.ball.xpos - self.ball.radius <= self.down_paddle.xpos + self.down_paddle.width:
                if self.ball.ypos + self.ball.radius == self.down_paddle.ypos:
                    self.ball.y_vel *= -1
                    
                    self.center_down_paddle = (self.down_paddle.xpos + self.down_paddle.width) / 2
                    self.difference_x = self.center_down_paddle - self.ball.xpos
                    self.reduction = (self.up_paddle.width / 2) / self.ball.max_vel
                    self.ball.x_vel = self.difference_x / self.reduction
                
      
    def startscreenloop(self):
        self.s.startscreen()

    def gameloop(self):
        self.s.gamescreen()
        self.score()
        self.ball.move()
        self.ball.reset()
        self.up_paddle.move()
        self.up_paddle.reset()
        self.down_paddle.move()
        self.down_paddle.reset()
        pygame.display.flip()
        #CONTINUE HERE
    
    def endscreenloop(self):
        pass
    
    def mainloop(self):
        self.startscreenloop()
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
    
    