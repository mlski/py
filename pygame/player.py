import pygame
from gameconfig import *

class Player:
    def __init__(self, obj_boundary):
        conf = GameConf()
        self.config = conf.config
        self.DISPLAY_WIDTH = int(self.config['game.config']['WINDOW_WIDTH'])
        self.DISPLAY_HEIGHT = int(self.config['game.config']['WINDOW_HEIGHT'])
        self.pos = pygame.Vector2(self.DISPLAY_WIDTH / 2, self.DISPLAY_HEIGHT / 2)
        self.avatar = pygame.image.load(os.path.dirname(__file__)+'/'+self.config['game.config']['AVATAR_FILE'])
        self.obj_boundary = obj_boundary
        self.player_boundary = pygame.Rect(self.pos.x, self.pos.y, self.avatar.get_width(), self.avatar.get_height())
        self.moveby = int(self.config['game.config']['MOVEBY'])
        self.score = 0
    
    def move_up(self):
        self.pos.y -= self.moveby
        self.player_boundary = pygame.Rect(self.pos.x, self.pos.y, self.avatar.get_width(), self.avatar.get_height())
    
    def move_down(self):
        self.pos.y += self.moveby
        self.player_boundary = pygame.Rect(self.pos.x, self.pos.y, self.avatar.get_width(), self.avatar.get_height())
    
    def move_left(self):
        self.pos.x -= self.moveby
        self.player_boundary = pygame.Rect(self.pos.x, self.pos.y, self.avatar.get_width(), self.avatar.get_height())
    
    def move_right(self):
        self.pos.x += self.moveby
        self.player_boundary = pygame.Rect(self.pos.x, self.pos.y, self.avatar.get_width(), self.avatar.get_height())
        
    def up_boundary(self):
        return self.pos.y >= 0

    def down_boundary(self):
        return self.pos.y <= self.DISPLAY_HEIGHT-self.avatar.get_height()
    
    def left_boundary(self):
        return self.pos.x >= 0
    
    def right_boundary(self):
        return self.pos.x <= self.DISPLAY_WIDTH-self.avatar.get_width()
        
    def get_pos(self):
        return (self.pos.x, self.pos.y)
    
    def colision(self):
        self.collision = self.player_boundary.colliderect(self.obj_boundary)
        if self.collision == True:
            self.score += 1
            print(f"Score: {self.score}")
            self.restart()
        return self.collision
    
    def restart(self):
        self.collision = False
        self.pos.x, self.pos.y = pygame.Vector2(self.DISPLAY_WIDTH / 2, self.DISPLAY_HEIGHT / 2)
        self.player_boundary = pygame.Rect(self.pos.x, self.pos.y, self.avatar.get_width(), self.avatar.get_height())
