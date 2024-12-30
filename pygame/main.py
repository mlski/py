import pygame
import sys
from playercontrol import *
from gameconfig import *
from graphicsdef import *
from gamecontrol import *

conf = GameConf()
config = conf.config

game = Game()

DISPLAY_WIDTH = int(config['game.config']['WINDOW_WIDTH'])
DISPLAY_HEIGHT = int(config['game.config']['WINDOW_HEIGHT'])
FPS = int(config['game.config']['FPS'])
MOVEBY = int(config['game.config']['MOVEBY'])

pygame.init()
window = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption(config['game.config']['GAME_NAME'])

player = Player()
player.set_window(window)
game.set_window(window)
game.set_player(player)
clock = pygame.time.Clock()
NEWOBSTACLE = pygame.USEREVENT + 1
pygame.time.set_timer(NEWOBSTACLE,1000)
running = True

while running:
    window.fill(BLACK)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        running = False
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == NEWOBSTACLE:
            game.draw_obstacle(window)
            
    game.draw_exitsign()
    
    window.blit(player.avatar, player.pos)
    
    font_score_table = pygame.font.Font('freesansbold.ttf', 20)
    font_score_number = pygame.font.Font('freesansbold.ttf', 40)
    font_game_over = pygame.font.Font('freesansbold.ttf', 100)

    collisions_text = font_score_table.render('Collisions', True, GREEN, BLUE)
    score_table = pygame.draw.rect(window, WHITE, (DISPLAY_WIDTH-100, 0, 100, 100))
    window.blit(collisions_text, score_table)
    
    score_text = font_score_number.render(str(player.score), True, BLACK)
    score_display = pygame.draw.rect(window, WHITE, (DISPLAY_WIDTH-65, 45, 40, 40))
    window.blit(score_text, score_display)
    
    if player.game_win == True:
        game_win_text = font_score_number.render("     YOU WON!", True, GREEN)
        game_win_display = pygame.draw.rect(window, WHITE, (400, 300, 405, 50))
        window.blit(game_win_text, game_win_display)
        
    if player.game_win == True and player.game_win_show_txt == False:
        player.win_game()
        
    if player.game_over == True:
        game_over_text = font_score_number.render("     GAME OVER!", True, RED)
        game_over_display = pygame.draw.rect(window, WHITE, (400, 300, 405, 50))
        window.blit(game_over_text, game_over_display)
        
    if player.score >= int(config['game.config']['MAX_COLLISIONS']) and player.game_over_snd_play == False:
        player.end_game()
    
    if not player.game_over and not player.game_win:
        if keys[pygame.K_LEFT] and player.left_boundary() and not player.collision_detection():
            player.move_left()
        if keys[pygame.K_RIGHT] and player.right_boundary() and not player.collision_detection():
            player.move_right()
        if keys[pygame.K_UP] and player.up_boundary() and not player.collision_detection():
            player.move_up()
        if keys[pygame.K_DOWN] and player.down_boundary() and not player.collision_detection():
            player.move_down()
    
    if keys[pygame.K_r]:
        player.restart()
    
    pygame.display.update()
    clock.tick(FPS)
    
pygame.quit();
sys.exit()