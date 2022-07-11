import random
class Stats():
    """отслеживание статистики"""

    def __init__(self):
        """инициализирует статистику"""
        self.reset_stats()
        self.run_game = True
        with open('high_score.txt', 'r') as f:
            self.high_score = int(f.readline().split()[0])


    def reset_stats(self):
        """статистика во время игры"""
        self.guns_left = 2
        self.score = 0
        self.level = 1
        self.bonus_gun = 0

    def get_bonus_position(self, b):
        return random.randint(0, b)