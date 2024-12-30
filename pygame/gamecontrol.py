from pygame import mixer
from pygame import image
import pygame
from gameconfig import *
from graphicsdef import *
import os
import random

class Game:
    def __init__(self):
        conf = GameConf()
        self.config = conf.config
        self.obs_x = random.randrange(int(self.config['game.config']['WINDOW_WIDTH'])-50)
        self.obs_y = random.randrange(int(self.config['game.config']['WINDOW_HEIGHT'])-50)
        self.obs_boundary = pygame.Rect(self.obs_x, self.obs_y, 40, 40)
        self.exitsign = image.load(os.path.dirname(__file__)+'/img/'+self.config['game.config']['EXITSIGN_FILE'])
        self.exitsign_boundary = pygame.Rect(0, 0, self.exitsign.get_width(), self.exitsign.get_height())
        
    def draw_exitsign(self):
        if self.window:
            self.exitsign = image.load(os.path.dirname(__file__)+'/img/'+self.config['game.config']['EXITSIGN_FILE'])
            self.exitsign_boundary = pygame.Rect(0, 0, self.exitsign.get_width(), self.exitsign.get_height())
            self.window.blit(self.exitsign, self.exitsign_boundary)
        
    def draw_obstacle(self, window):
        self.window = self.window or window
        if self.window:
            self.obs_x = random.randrange(int(self.config['game.config']['WINDOW_WIDTH'])-50)
            self.obs_y = random.randrange(int(self.config['game.config']['WINDOW_HEIGHT'])-50)
            pygame.draw.circle(self.window, RED, (self.obs_x, self.obs_y), 40)
            self.obs_boundary = pygame.Rect(self.obs_x, self.obs_y, 40, 40)
            #print(f"OX: {self.obs_x}, OY: {self.obs_y}, BOUNDARY: {self.obs_boundary}")
    
    def set_window(self, window):
        self.window = window
    
    def set_player(self, player):
        self.player = player
    
    def play_game_over_sound(self, player):
        player.game_over_snd_play = True
        if self.config['game.config']['SOUNDS'] == 'on':
            mixer.init()
            mixer.music.load(os.path.dirname(__file__)+'/snd/'+self.config['game.config']['GAME_OVER_SOUND'])
            mixer.music.set_volume(1.0)
            mixer.music.play()
        player.game_over_snd_play = False
    
    def play_game_win_sound(self, player):
        player.game_win_show_txt = False
        if self.config['game.config']['SOUNDS'] == 'on':
            mixer.init()
            mixer.music.load(os.path.dirname(__file__)+'/snd/'+self.config['game.config']['GAME_WIN_SOUND'])
            mixer.music.set_volume(1.0)
            mixer.music.play()
        player.game_win_show_txt = False
            
    