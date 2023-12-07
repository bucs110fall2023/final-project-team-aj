import pygame
import random
import math

from src.ball import Ball
from src.paddle import Paddle
from src.obstacle import Obstacle

class Controller:
    def __init__(self, red_score=0, blue_score=0):
        pygame.init()
        buffer = 10
        ball_radius = 30
        self.window_width = 750
        self.window_height = 800
        self.green = (6, 168, 0)
        obstacle_long = 75
        obstacle_thin = 2
        

        self.screen = pygame.display.set_mode([self.window_width, self.window_height])
        self.ball = Ball(self.window_width / 2, self.window_height / 2 - (ball_radius / 2), ball_radius)
        self.sample_paddle = Paddle()
        self.red_paddle = Paddle((self.window_width / 2) - (self.sample_paddle.width / 2), buffer, "red")
        self.blue_paddle = Paddle((self.window_width / 2) - (self.sample_paddle.width / 2), (self.window_height - buffer - self.sample_paddle.height), "blue")
        self.obstacle1_top = Obstacle((self.window_width - obstacle_long - 100), .4*(self.window_height) - .5*(obstacle_long), obstacle_long, obstacle_thin)
        self.obstacle1_right = Obstacle((self.window_width - 100), .4*(self.window_height) - .5*(obstacle_long), obstacle_thin, obstacle_long)
        self.obstacle1_left = Obstacle((self.window_width - obstacle_long - 100), .4*(self.window_height) - .5*(obstacle_long), obstacle_thin, obstacle_long)
        self.obstacle1_bottom = Obstacle((self.window_width - obstacle_long - 100), .4*(self.window_height) - .5*(obstacle_long) + obstacle_long, obstacle_long, obstacle_thin)
        self.obstacle2_top = Obstacle(100, .6*(self.window_height) - .5*(obstacle_long), obstacle_long, obstacle_thin)
        self.obstacle2_right = Obstacle(100 + obstacle_long, .6*(self.window_height) - .5*(obstacle_long), obstacle_thin, obstacle_long)
        self.obstacle2_left = Obstacle(100, .6*(self.window_height) - .5*(obstacle_long), obstacle_thin, obstacle_long)
        self.obstacle2_bottom = Obstacle(100, .6*(self.window_height) - .5*(obstacle_long) + obstacle_long, obstacle_long, obstacle_thin)
        
        self.red_score = red_score
        self.blue_score = blue_score
        
        self.allsprites = pygame.sprite.Group()
        self.allsprites.add(self.ball)
        self.allsprites.add(self.red_paddle)
        self.allsprites.add(self.blue_paddle)
        self.allsprites.add(self.obstacle1_top)
        self.allsprites.add(self.obstacle1_right)
        self.allsprites.add(self.obstacle1_left)
        self.allsprites.add(self.obstacle1_bottom)
        self.allsprites.add(self.obstacle2_top)
        self.allsprites.add(self.obstacle2_right)
        self.allsprites.add(self.obstacle2_left)
        self.allsprites.add(self.obstacle2_bottom)
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
            text = font.render("Press space to start each round", True, "white")
            instrustart_text_x_pos = 0
            instrustart_text_y_pos = instruwin_text_y_pos + space_bw_text
            self.screen.blit(text, (instrustart_text_x_pos, instrustart_text_y_pos))
            pygame.display.flip()

    def score(self):
        font = pygame.font.Font(None, 48)
        self.red_score_text = font.render(f"{self.red_score}", True, "red")
        self.blue_score_text = font.render(f"{self.blue_score}", True, "blue")
        self.screen.blit(self.red_score_text, (3, self.window_height / 4))
        self.screen.blit(self.blue_score_text, (self.window_width - 20, 3 * (self.window_height / 4)))
        
    def gameloop(self):   
        game_to = 3    
        while self.state == "GAME":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = "QUIT"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        direction = 0 
                        if random.randint(-10, 10) > 0:
                            direction = 1
                        if random.randint(-10, 10) < 0:
                            direction = -1
                        self.ball.y_vel = self.ball.max_vel * direction
                    if event.key == pygame.K_1:
                        self.ball.x_vel = 2 * math.cos(math.radians(15))
                        self.ball.y_vel = - 2 * math.sin(math.radians(15))
                    if event.key == pygame.K_2:
                        self.ball.x_vel = - 2 * math.cos(math.radians(15))
                        self.ball.y_vel = 2 * math.sin(math.radians(15))
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
            if self.red_score >= game_to or self.blue_score >= game_to:
                self.state = "END"
                    
            
            self.screen.fill(self.green)
            pygame.draw.line(self.screen, "white", (0, self.window_height / 2), (self.window_width, self.window_height / 2), 2)
            self.allsprites.draw(self.screen)
            self.ball.move()
            self.score()
            
            if self.red_paddle.rect.x < 0:
                self.red_paddle.rect.x = 0
            if self.red_paddle.rect.x > self.window_width - self.red_paddle.width:
                self.red_paddle.rect.x = self.window_width - self.red_paddle.width
            if self.blue_paddle.rect.x < 0:
                self.blue_paddle.rect.x = 0
            if self.blue_paddle.rect.x > self.window_width - self.blue_paddle.width:
                self.blue_paddle.rect.x = self.window_width - self.blue_paddle.width
            
            if pygame.sprite.collide_rect(self.ball, self.blue_paddle):
                self.ball.y_vel *= -1
                self.ball.x_vel = random.uniform(-1, 1)
            if pygame.sprite.collide_rect(self.ball, self.red_paddle):
                self.ball.y_vel *= -1
                self.ball.x_vel = random.uniform(-1, 1)
                
            if pygame.sprite.collide_rect(self.ball, self.obstacle1_top):
                self.ball.y_vel *= -1
            if pygame.sprite.collide_rect(self.ball, self.obstacle2_top):
                self.ball.y_vel *= -1
            if pygame.sprite.collide_rect(self.ball, self.obstacle1_bottom):
                self.ball.y_vel *= -1
            if pygame.sprite.collide_rect(self.ball, self.obstacle2_bottom):
                self.ball.y_vel *= -1
            if pygame.sprite.collide_rect(self.ball, self.obstacle1_right):
                self.ball.x_vel *= -1
            if pygame.sprite.collide_rect(self.ball, self.obstacle2_right):
                self.ball.x_vel *= -1
            if pygame.sprite.collide_rect(self.ball, self.obstacle1_left):
                self.ball.x_vel *= -1
            if pygame.sprite.collide_rect(self.ball, self.obstacle2_left):
                self.ball.x_vel *= -1
             
            if self.ball.rect.x < 0:
                self.ball.x_vel *= -1
            if self.ball.rect.x > self.window_width - self.ball.radius:
                self.ball.x_vel *= -1
                
            if self.ball.rect.y < self.red_paddle.rect.y:
                self.blue_score += 1
                self.ball.reset()
                self.red_paddle.reset()
                self.blue_paddle.reset()
            if self.ball.rect.y > self.blue_paddle.rect.y + self.blue_paddle.height:
                self.red_score += 1
                self.ball.reset()
                self.red_paddle.reset()
                self.blue_paddle.reset()
                
            pygame.display.flip()

    def endscreenloop(self):
        while self.state == "END":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = "QUIT"
            
            if self.red_score >= self.blue_score:
                winner = "RED"
            elif self.red_score <= self.blue_score:
                winner = "BLUE"
                
            self.screen.fill(self.green)
            font = pygame.font.Font(None, 100)
            text = font.render(f"TEAM {winner} WINS!", True, "white")
            winner_text_rect = text.get_rect()
            half_text_width = winner_text_rect.width // 2
            half_text_height = winner_text_rect.height // 2
            winner_text_x_pos = (self.window_width // 2) - half_text_width
            winner_text_y_pos = (self.window_height // 4) - half_text_height
            winner_text_rect_center = (winner_text_x_pos, winner_text_y_pos)
            self.screen.blit(text, winner_text_rect_center)
        
            pygame.display.flip()

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

