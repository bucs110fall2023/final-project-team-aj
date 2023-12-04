import pygame

class Screens:
    def __init__(self):
        pygame.init()
        self.window_width = 750
        self.window_height = 800
        self.screen = pygame.display.set_mode([self.window_width, self.window_height])
        
    def startscreen(self):
        self.screen_color = (6, 168, 0)
        self.screen.fill(self.screen_color)
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
        text = font.render("PRESS START", True, "white")
        starttext_rect = text.get_rect()
        half_text_width = starttext_rect.width // 2
        half_text_height = starttext_rect.height // 2
        starttext_x_pos = (self.window_width // 2) - half_text_width
        starttext_y_pos = self.window_height - (self.window_height // 3)
        starttext_rect_center = (starttext_x_pos, starttext_y_pos)
        self.screen.blit(text, starttext_rect_center)
        self.starttext_hitbox = pygame.Rect(starttext_x_pos, starttext_y_pos, starttext_rect.width, starttext_rect.height)
        
        pygame.display.flip()
        
    def gamescreen(self):
        self.screen_color = (6, 168, 0)
        self.screen.fill(self.screen_color)
        pygame.draw.line(self.screen, "white", (0, self.window_height/2), (self.window_width, self.window_height/2), 2)
        
        pygame.display.flip()