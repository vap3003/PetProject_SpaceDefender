import pygame

class Bonus_gun(pygame.sprite.Sprite):
    """добавление бонусов в игру"""

    def __init__(self, screen):
        super(Bonus_gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/bonus_gun.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speed = 0.1
        self.bonus = 0

    def draw(self):
        """вывод пришельца на экран"""
        self.screen.blit(self.image, self.rect)


    def update(self):
        """Перемещает пришельцев"""
        self.y += self.speed
        self.rect.y = self.y

class Bonus_life(pygame.sprite.Sprite):
    """добавление бонусов в игру"""

    def __init__(self, screen):
        super(Bonus_life, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/bonus_life.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speed = 0.1
        self.bonus = 1

    def draw(self):
        """вывод пришельца на экран"""
        self.screen.blit(self.image, self.rect)


    def update(self):
        """Перемещает пришельцев"""
        self.y += self.speed
        self.rect.y = self.y