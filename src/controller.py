import pygame
from src.screens import Screens
from src.ball import Ball
from src.paddle import Paddle

class Controller:
    
    def __init__(self, red_score=0, blue_score=0):
        pygame.init()
        buffer = 10
        self.s = Screens()
        self.ball = Ball(self.s.window_width / 2, self.s.window_height / 2, 10)
        self.sample_paddle = Paddle()
        self.red_paddle = Paddle((self.s.window_width / 2) - self.sample_paddle.width, buffer, "red")
        self.blue_paddle = Paddle((self.s.window_width / 2) - self.sample_paddle.width, self.s.window_height - buffer - self.sample_paddle.height, "blue")
        self.red_score = red_score
        self.blue_score = blue_score
        self.state = "HOME"
        
    def score(self):
        font = pygame.font.Font(None, 48)
        self.red_score_text = font.render(f"{self.red_score}", True, "red")
        self.blue_score_text = font.render(f"{self.blue_score}", True, "blue")
        self.s.screen.blit(self.red_score_text, (5, self.s.window_height/4))
        self.s.screen.blit(self.blue_score_text, (self.s.window_width - 20, 3*(self.s.window_height/4)))
    
    def collisions(self):
        if self.ball.xpos - self.ball.radius == 0:
            self.ball.x_vel *= -1
        elif self.ball.xpos + self.ball.radius == self.s.window_width:
            self.ball.x_vel *= -1
            
        if self.ball.y_vel < 0:
            if self.ball.xpos + self.ball.radius >= self.red_paddle.xpos and self.ball.xpos - self.ball.radius <= self.red_paddle.xpos + self.red_paddle.width:
                if self.ball.ypos - self.ball.radius == self.red_paddle.ypos + self.red_paddle.height:
                    self.ball.y_vel *= -1
                    
                    self.center_red_paddle = (self.red_paddle.xpos + self.red_paddle.width) / 2
                    self.difference_x = self.center_red_paddle - self.ball.xpos
                    self.reduction = (self.red_paddle.width / 2) / self.ball.max_vel
                    self.ball.x_vel = self.difference_x / self.reduction
                    
        else:
            if self.ball.xpos + self.ball.radius >= self.blue_paddle.xpos and self.ball.xpos - self.ball.radius <= self.blue_paddle.xpos + self.blue_paddle.width:
                if self.ball.ypos + self.ball.radius == self.blue_paddle.ypos:
                    self.ball.y_vel *= -1
                    
                    self.center_blue_paddle = (self.blue_paddle.xpos + self.blue_paddle.width) / 2
                    self.difference_x = self.center_blue_paddle - self.ball.xpos
                    self.reduction = (self.red_paddle.width / 2) / self.ball.max_vel
                    self.ball.x_vel = self.difference_x / self.reduction
                
      
    def startscreenloop(self):
        self.s.startscreen()

    def gameloop(self):
        self.s.gamescreen()
        self.score()
        self.ball.move()
        self.ball.reset()
        self.red_paddle.move()
        self.red_paddle.reset()
        self.blue_paddle.move()
        self.blue_paddle.reset()
        pygame.display.flip()
        #CONTINUE HERE
    
    def endscreenloop(self):
        self.s.endscreen()
        # if self.red_score > self.blue_score:
        #     winner = "RED"
        # elif self.red_score < self.blue_score:
        #     winner = "BLUE"
    
    def mainloop(self):
        self.gameloop()
        # while self.state == "HOME":
        #     self.startscreenloop()
        #     for event in pygame.event.get():
        #         if event.type == pygame.KEYDOWN:
        #             if event.key == pygame.K_SPACE:
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
        
        
    
    