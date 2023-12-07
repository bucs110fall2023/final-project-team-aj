import pygame
import random

from src.ball import Ball
from src.paddle import Paddle

class Controller:
    def __init__(self, red_score=0, blue_score=0):
        pygame.init()
        buffer = 10
        self.window_width = 750
        self.window_height = 800
        self.green = (6, 168, 0)

        self.screen = pygame.display.set_mode([self.window_width, self.window_height])
        self.ball = Ball(self.window_width / 2, self.window_height / 2, 30)
        self.sample_paddle = Paddle()

        self.red_paddle = Paddle((self.window_width / 2) - (self.sample_paddle.width / 2), buffer, "red")
        self.blue_paddle = Paddle((self.window_width / 2) - (self.sample_paddle.width / 2), (self.window_height - buffer - self.sample_paddle.height), "blue")
        self.red_score = red_score
        self.blue_score = blue_score
        self.allsprites = pygame.sprite.Group()
        self.allsprites.add(self.ball)
        self.allsprites.add(self.red_paddle)
        self.allsprites.add(self.blue_paddle)
        self.state = "HOME"
        
    def startscreenloop(self):
        while self.state == "HOME":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = "QUIT"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.state = "GAME"
                    if event.key == pygame.K_ESCAPE:
                        self.state = "QUIT"

            self.screen.fill(self.green)
            font = pygame.font.Font(None, 100)
            text = font.render("PADDLES", True, "white")
            intro_text_rect = text.get_rect()
            half_text_width = intro_text_rect.width // 2
            half_text_height = intro_text_rect.height // 2
            intro_text_x_pos = (self.window_width // 2) - half_text_width
            intro_text_y_pos = (self.window_height // 4) - half_text_height
            intro_text_rect_center = (intro_text_x_pos, intro_text_y_pos)
            self.screen.blit(text, intro_text_rect_center)

            font = pygame.font.Font(None, 48)
            text = font.render("By: Aaron Damsky and Joseph Kessler", True, "white")
            text_rect = text.get_rect()
            half_text_width = text_rect.width // 2
            half_text_height = text_rect.height // 2
            creators_text_x_pos = (self.window_width // 2) - half_text_width
            creators_text_y_pos = intro_text_y_pos + intro_text_rect.height
            creators_text_rect_center = (creators_text_x_pos, creators_text_y_pos)
            self.screen.blit(text, creators_text_rect_center)

            font = pygame.font.Font(None, 60)
            text = font.render("PRESS SPACE TO START", True, "white")
            starttext_rect = text.get_rect()
            half_text_width = starttext_rect.width // 2
            half_text_height = starttext_rect.height // 2
            starttext_x_pos = (self.window_width // 2) - half_text_width
            starttext_y_pos = self.window_height - (self.window_height // 2)
            starttext_rect_center = (starttext_x_pos, starttext_y_pos)
            self.screen.blit(text, starttext_rect_center)

            space_bw_text = 30
            font = pygame.font.Font(None, 30)
            text = font.render("Instructions:", True, "white")
            instru_text_x_pos = 0
            instru_text_y_pos = self.window_height - (self.window_height / 3)
            self.screen.blit(text, (instru_text_x_pos, instru_text_y_pos))
            text = font.render("Team Blue: use the arrow keys to move your paddle left and right", True, "white")
            instrublue_text_x_pos = 0
            instrublue_text_y_pos = instru_text_y_pos + space_bw_text
            self.screen.blit(text, (instrublue_text_x_pos, instrublue_text_y_pos))
            text = font.render("Team Red: use the a and d keys to move your paddle left and right", True, "white")
            instrured_text_x_pos = 0
            instrured_text_y_pos = instrublue_text_y_pos + space_bw_text
            self.screen.blit(text, (instrured_text_x_pos, instrured_text_y_pos))
            text = font.render("Try to get the ball past the opposing teams paddle", True, "white")
            instrugoal_text_x_pos = 0
            instrugoal_text_y_pos = instrured_text_y_pos + space_bw_text
            self.screen.blit(text, (instrugoal_text_x_pos, instrugoal_text_y_pos))
            text = font.render("First team to 7 points wins!", True, "white")
            instruwin_text_x_pos = 0
            instruwin_text_y_pos = instrugoal_text_y_pos + space_bw_text
            self.screen.blit(text, (instruwin_text_x_pos, instruwin_text_y_pos))
            pygame.display.flip()

    def score(self):
        font = pygame.font.Font(None, 48)
        self.red_score_text = font.render(f"{self.red_score}", True, "red")
        self.blue_score_text = font.render(f"{self.blue_score}", True, "blue")
        self.screen.blit(self.red_score_text, (5, self.window_height / 4))
        self.screen.blit(self.blue_score_text, (self.window_width - 20, 3 * (self.window_height / 4)))
        
    def gameloop(self):        
        while self.state == "GAME":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = "QUIT"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.ball.y_vel = self.ball.max_vel
                    if event.key == pygame.K_ESCAPE:
                        self.state = "QUIT"
                    if event.key == pygame.K_a:
                        self.red_paddle.move("left")
                    if event.key == pygame.K_d:
                        self.red_paddle.move("right")
                    if event.key == pygame.K_LEFT:
                        self.blue_paddle.move("left")
                    if event.key == pygame.K_RIGHT:
                        self.blue_paddle.move("right")
            
            self.screen.fill(self.green)
            pygame.draw.line(self.screen, "white", (0, self.window_height / 2), (self.window_width, self.window_height / 2), 2)
            self.allsprites.draw(self.screen)
            self.ball.move()
            
            if pygame.sprite.collide_rect(self.ball, self.blue_paddle):
                self.ball.y_vel *= -1
                self.ball.x_vel += random.uniform(-1, 1)
            if pygame.sprite.collide_rect(self.ball, self.red_paddle):
                self.ball.y_vel *= -1
                
            if self.ball.rect.x < 0:
                self.ball.x_vel *= -1
            if self.ball.rect.x > self.window_width:
                self.ball.x_vel *= -1
                
            pygame.display.flip()

    def endscreenloop(self):
        pass

    def mainloop(self):
        while self.state != "QUIT":
            if self.state == "HOME":
                self.startscreenloop()
            elif self.state == "GAME":
                self.gameloop()
            elif self.state == "END":
                self.endscreenloop()
            else:
                print("Invalid state")

