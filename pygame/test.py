import pygame
import sys
from player import *
from gameconfig import *

conf = GameConf()
config = conf.config

DISPLAY_WIDTH = int(config['game.config']['WINDOW_WIDTH'])
DISPLAY_HEIGHT = int(config['game.config']['WINDOW_HEIGHT'])
FPS = int(config['game.config']['FPS'])
MOVEBY = int(config['game.config']['MOVEBY'])
BLACK = (0, 0, 0)

pygame.init()
window = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption(config['game.config']['GAME_NAME'])

player = Player()
clock = pygame.time.Clock()
running = True

while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if keys[pygame.K_q]:
        running = False
    
    window.fill(BLACK)
    
    window.blit(player.avatar, player.pos)
    
    if keys[pygame.K_LEFT] and player.left_boundary():
        player.move_left()
    if keys[pygame.K_RIGHT] and player.right_boundary():
        player.move_right()
    if keys[pygame.K_UP] and player.up_boundary():
       player.move_up()
    if keys[pygame.K_DOWN] and player.down_boundary():
        player.move_down()
    
    pygame.display.update()
    clock.tick(FPS)
    
pygame.quit();
sys.exit()