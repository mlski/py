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
WHITE = (255, 255,255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

pygame.init()
window = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption(config['game.config']['GAME_NAME'])
obj_pos1 = (100, 100)
obj_boundary = pygame.Rect(100, 100, 40, 40)

player = Player(obj_boundary)
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
    pygame.draw.circle(window, WHITE, obj_pos1, 40)
    score_table = pygame.draw.rect(window, WHITE, (DISPLAY_WIDTH-100, 0, 100, 100))
    font_score_table = pygame.font.Font('freesansbold.ttf', 20)
    font_score_number = pygame.font.Font('freesansbold.ttf', 40)
    text = font_score_table.render('Collisions', True, GREEN, BLUE)
    window.blit(text, score_table)
    score = font_score_number.render(str(player.score), True, BLACK)
    score_display = pygame.draw.rect(window, WHITE, (DISPLAY_WIDTH-65, 45, 40, 40))
    window.blit(score, score_display)

    
    if keys[pygame.K_LEFT] and player.left_boundary() and not player.colision():
        player.move_left()
    if keys[pygame.K_RIGHT] and player.right_boundary() and not player.colision():
        player.move_right()
    if keys[pygame.K_UP] and player.up_boundary() and not player.colision():
       player.move_up()
    if keys[pygame.K_DOWN] and player.down_boundary() and not player.colision():
        player.move_down()
    
    if keys[pygame.K_r]:
        player.restart()
    
    pygame.display.update()
    clock.tick(FPS)
    
pygame.quit();
sys.exit()