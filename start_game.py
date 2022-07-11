import pygame, controls, menu
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from score import Scores

def run():
    screen = pygame.display.set_mode((500, 700))
    pygame.display.set_caption("Space Defender")
    bg_color = (73, 78, 82)
    gun = Gun(screen)
    bullets = Group()
    enemies = Group()
    stats = Stats()
    bonus = Group()
    game_info = Scores(screen, stats)
    controls.create_army(screen, enemies, stats, bonus)
    while True:
        controls.events(screen, gun, bullets, stats, game_info)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, stats, game_info, gun, enemies, bullets, bonus)
            controls.update_bullets(screen, stats, game_info, enemies, bullets, bonus)
            controls.update_inos(stats, screen, game_info, gun, enemies, bullets, bonus)