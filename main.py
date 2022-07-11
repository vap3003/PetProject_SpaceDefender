import pygame, menu
from stats import Stats
from score import Scores

def go():
    pygame.init()
    screen = pygame.display.set_mode((500, 700))
    pygame.display.set_caption("Space Defender")
    stats = Stats()
    game_info = Scores(screen, stats)
    menu.show_menu(screen, game_info)

go()