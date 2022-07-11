import pygame, sys
from bullet import Bullet, Bonus_Bullet
from enemy import Enemy
from bonus import Bonus_gun, Bonus_life
import time
import random

def events(screen, gun, bullets, stats, game_info):
    """обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.mright = True
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
# добавить проверку на бонусную пулю
                if stats.bonus_gun > 0:
                    new_bullet = Bonus_Bullet(screen, gun)
                    game_info.image_bonus_bullet_left()
                    bullets.add(new_bullet)
                    stats.bonus_gun -= 1
                else:
                    new_bullet = Bullet(screen, gun)
                    bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = False

def update(bg_color, screen, stats, game_info, gun, enemies, bullets, bonus):
    """обновление экрана"""
    screen.fill(bg_color)
    game_info.show_score()
    game_info.image_level()
    game_info.image_high_score()
    game_info.image_bonus_bullet_left()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    enemies.draw(screen)
    bonus.draw(screen)
    pygame.display.flip()

def update_bullets(screen, stats, game_info, enemies, bullets, bonus):
    """обновлять позиции пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)
    if collisions:
        for enemies in collisions.values():
            stats.score += 10 * len(enemies)
        game_info.image_score()
        check_high_score(stats, game_info)
        game_info.image_lives()
    collisions = pygame.sprite.groupcollide(bullets, bonus, True, True)

    if collisions:
        for bonus in collisions.values():
            print(bonus)
            if bonus[0].bonus == 1:
                stats.guns_left += 1
            else:
                stats.bonus_gun = 10
        game_info.image_score()
        check_high_score(stats, game_info)
        game_info.image_lives()
    if len(enemies) == 0:
        stats.level += 1
        bullets.empty()
        bonus.empty()
        create_army(screen, enemies, stats, bonus)

def gun_kill(stats, screen, game_info, gun, enemies, bullets, bonus):
    """столкновение пушки и армии"""
    if stats.guns_left > 0:
        stats.guns_left -= 1
        game_info.image_lives()
        enemies.empty()
        bonus.empty()
        bullets.empty()
        create_army(screen, enemies, stats, bonus)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()

def update_inos(stats, screen, game_info, gun, enemies, bullets, bonus):
    """Обновляет позицию пришельцев"""
    enemies.update()
    bonus.update()
    if pygame.sprite.spritecollideany(gun, enemies):
        gun_kill(stats, screen, game_info, gun, enemies, bullets, bonus)
    inos_check(stats, screen, game_info, gun, enemies, bullets, bonus)

def inos_check(stats, screen, game_info, gun, enemies, bullets, bonus):
    """ добралась ли армия до края"""
    screen_rect = screen.get_rect()
    for ino in enemies.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, game_info, gun, enemies, bullets, bonus)
            break;

def create_army(screen, enemies, stats, bonus):
    """создание армии пришельцев"""
    allien = Enemy(screen)
    allien_width = allien.rect.width
    number_allien_x = int((500 - 2 * (allien_width)) / (allien_width + 10))
    print(number_allien_x)
    allien_height = allien.rect.height
    number_allien_y = int((700 - 300 - 2 * (allien_height + 10)) / (allien_height + 10))
    print(number_allien_y)
    print((500 - 2 * allien_width - (allien_width * number_allien_x))/(number_allien_x - 1))
    bonus_position = stats.get_bonus_position((number_allien_y - 1) * (number_allien_x - 1))
    if stats.guns_left < 3 and random.randint(0, 1) and stats.level > 1:
        bonus_life_position = stats.get_bonus_position((number_allien_y - 1) * (number_allien_x - 1))
        while bonus_position == bonus_life_position:
            bonus_life_position = stats.get_bonus_position((number_allien_y - 1) * (number_allien_x - 1))
    else:
        bonus_life_position = -1
    for row_number in range(number_allien_y):
        for allien_number in range(number_allien_x):
            if allien_number + row_number * number_allien_x == bonus_position:
                allien = Bonus_gun(screen)
                allien.speed = 0.1 + 0.05 * (stats.level // 2)
                allien.x = allien_width + (allien_width + (500 - 2 * allien_width - (allien_width * number_allien_x)) / (number_allien_x - 1)) * allien_number
                allien.y = 100 + (allien_height + 10) + (allien_height + 10) * row_number
                allien.rect.x = allien.x + 10
                allien.rect.y = allien.rect.height + 10 + 2 * allien.rect.height * row_number
                bonus.add(allien)
            elif allien_number + row_number * number_allien_x == bonus_life_position:
                allien = Bonus_life(screen)
                allien.speed = 0.1 + 0.05 * (stats.level // 2)
                allien.x = allien_width + (
                allien_width + (500 - 2 * allien_width - (allien_width * number_allien_x)) / (number_allien_x - 1)) * allien_number
                allien.y = 100 + (allien_height + 10) + (allien_height + 10) * row_number
                allien.rect.x = allien.x + 10
                allien.rect.y = allien.rect.height + 10 + 2 * allien.rect.height * row_number
                bonus.add(allien)
            else:
                allien = Enemy(screen)
                allien.speed = 0.1 + 0.05 * (stats.level // 2)
                allien.x = allien_width + (allien_width + (500 - 2 * allien_width - (allien_width * number_allien_x))/(number_allien_x - 1)) * allien_number
                allien.y = 100 + (allien_height + 10) + (allien_height + 10) * row_number
                allien.rect.x = allien.x + 10
                allien.rect.y = allien.rect.height + 10 + 2 * allien.rect.height * row_number
                enemies.add(allien)
            print(allien.bonus)

def check_high_score(stats, game_info):
    """"проверка нового рекорда"""
    if stats.score > stats.high_score:
        game_info.new_record_color = (255, 250, 84)
        stats.high_score = stats.score
        game_info.image_high_score()
        with open('high_score.txt', 'w') as f:
            f.write(str(stats.high_score))

# def events(screen, gun, bullets, stats, game_info):
#     """обработка событий"""
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_d:
#                 gun.mright = True
#             elif event.key == pygame.K_a:
#                 gun.mleft = True
#             elif event.key == pygame.K_SPACE:
# # добавить проверку на бонусную пулю
#                 if stats.bonus_gun > 0:
#                     new_bullet = Bonus_Bullet(screen, gun)
#                     game_info.image_bonus_bullet_left()
#                     bullets.add(new_bullet)
#                     stats.bonus_gun -= 1
#                 else:
#                     new_bullet = Bullet(screen, gun)
#                     bullets.add(new_bullet)
#         elif event.type == pygame.KEYUP:
#             if event.key == pygame.K_d:
#                 gun.mright = False
#             elif event.key == pygame.K_a:
#                 gun.mleft = False