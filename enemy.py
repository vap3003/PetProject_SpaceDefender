import pygame

class Enemy(pygame.sprite.Sprite):
    """класс одного пришельца"""

    def __init__(self, screen):
        """инициализируем и задаем начальную позицию"""
        super(Enemy, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/alien.png')
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
