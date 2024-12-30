import pygame
from gameconfig import *
from gamecontrol import *

class Player:
    def __init__(self):
        conf = GameConf()
        self.config = conf.config
        self.game = Game()
        self.DISPLAY_WIDTH = int(self.config['game.config']['WINDOW_WIDTH'])
        self.DISPLAY_HEIGHT = int(self.config['game.config']['WINDOW_HEIGHT'])
        self.pos = pygame.Vector2(self.DISPLAY_WIDTH / 2, self.DISPLAY_HEIGHT / 2)
        self.avatar = pygame.image.load(os.path.dirname(__file__)+'/img/'+self.config['game.config']['AVATAR_FILE'])
        self.player_boundary = pygame.Rect(self.pos.x, self.pos.y, self.avatar.get_width(), self.avatar.get_height())
        self.moveby = int(self.config['game.config']['MOVEBY'])
        self.score = 0
        self.game_over = False
        self.game_over_snd_play = False
        self.game_win_show_txt = False
        self.game_win = False
    
    def set_window(self, window):
        self.window = window
    
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
    
    def collision_detection(self):
        self.game = Game()
        self.collision = self.player_boundary.colliderect(self.game.obs_boundary)
        self.win_check = self.player_boundary.colliderect(self.game.exitsign_boundary)
        if self.win_check == True:
            self.game_win = True
            return self.game_win
        if self.collision == True:
            self.score += 1
        return self.collision
    
    def end_game(self):
        self.collision = True
        self.game_over = True
        self.score = 0
        self.game.play_game_over_sound(self)
    
    def win_game(self):
        self.game_win = True
        self.game.play_game_win_sound(self)
    
    def refresh_position(self):
        self.collision = True
        self.pos.x, self.pos.y = pygame.Vector2(self.DISPLAY_WIDTH / 2, self.DISPLAY_HEIGHT / 2)
        self.player_boundary = pygame.Rect(self.pos.x, self.pos.y, self.avatar.get_width(), self.avatar.get_height())
    
    def restart(self):
        self.game_over = False
        self.game_win = False
        self.score = 0
        self.refresh_position()
