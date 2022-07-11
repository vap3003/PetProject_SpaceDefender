import pygame.font
from bonus import Bonus_life
from pygame.sprite import Group

class Scores():
    """вывод игровой информации"""

    def __init__(self, screen, stats):
        """инициализируем подсчет очков"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (247, 249, 238)
        self.new_record_color = (247, 249, 238)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_high_score()
        self.image_lives()
        self.image_level()
        self.image_bonus_bullet_left()

    def image_score(self):
        """преобразовывает текст счета в графическое изображение"""
        self.score_img = self.font.render(str(self.stats.score), True, self.new_record_color, (73, 78, 82))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 65

    def show_score(self):
        """вывод счета на экран"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.lives.draw(self.screen)

    def image_high_score(self):
        """отображение максимального рекорда"""
        self.high_score_image = self.font.render('TOP ' + str(self.stats.high_score), True, self.text_color, (73, 78, 82))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.right - 40
        self.high_score_rect.top = 30

    def image_lives(self):
        """количество жизней"""
        self.lives = Group()
        for life_number in range(self.stats.guns_left):
            life = Bonus_life(self.screen)
            life.rect.x = 20 + life_number * (life.rect.width + 20)
            life.rect.y = 20
            self.lives.add(life)

    def image_level(self):
        """отображение игрового уровня"""
        self.level_image = self.font.render('LVL ' + str(self.stats.level), True, self.text_color, (73, 78, 82))
        self.level_rect = self.level_image.get_rect()
        self.level_rect.centerx = self.screen_rect.centerx
        self.level_rect.top = self.screen_rect.top + 30

    def image_bonus_bullet_left(self):
        """количество жизней"""
        self.rect = pygame.Rect(0, 0, 9 * self.stats.bonus_gun, 20)
        self.color = 255, 91, 76
        self.rect.x = 20
        self.rect.y = 65
        pygame.draw.rect(self.screen, self.color, self.rect)
