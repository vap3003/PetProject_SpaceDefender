import pygame, sys
import pygame.font
import start_game


def show_menu(screen, game_info):
    menu_background = pygame.image.load('images/menu.jpg')
    start_button = Button(screen)
    show_records_button = Button(screen)
    show = True
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(menu_background, (0, 0))
        if start_button.draw(320, 'START GAME') == 2:
            start_game.run()
        if show_records_button.draw(370, 'RECORDS') == 2:
            show_records(screen, game_info)
        pygame.display.update()

def show_records(screen, game_info):
    screen_rect = screen.get_rect()
    menu_background = pygame.image.load('images/menu_records.jpg')
    show = True
    back_button = Button(screen)
    #game_info.image_high_score()
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(menu_background, (0, 0))
        with open('high_score.txt', 'r') as f:
            font = pygame.font.SysFont(None, 36)
            for i in range(5):
                record = f.readline()
                record_image = font.render(str(i+1) +'. ' + record.split('\n')[0], True, (255, 255, 255))
                record_image.set_alpha(300)
                record_rect = record_image.get_rect()
                record_rect.centerx = screen_rect.centerx
                record_rect.top = 320 + 40 * i
                screen.blit(record_image, record_rect)
                #pygame.time.delay(3000)
            if back_button.draw(525, 'GO BACK') == 2:
                show_menu(screen, game_info)
        pygame.display.flip()




class Button:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width = 100
        self.height = 20
        #self.rect.centerx = self.screen_rect.centerx
        self.inactive_color = (250, 105, 76)
        self.active_color = (255, 255, 255)

    def draw(self, y, message):
        self.height = text_height(message) + 20
        self.width = text_width(message) + 20
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        x = self.screen_rect.centerx - self.width/2
        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(self.screen,  self.active_color, (x, y, self.width, self.height))
                print_text(self.screen, message, y, self.height, (73, 78, 82))
                if click[0] == 1:
                    return 2
                #     pygame.mixer.Sound.play(button_sound)
                #     pygame.time.delay(300)
                #     action()
            else:
                pygame.draw.rect(self.screen, self.inactive_color, (x, y, self.width, self.height))
                print_text(self.screen, message, y, self.height, (255, 255, 255))
        else:
            pygame.draw.rect(self.screen, self.inactive_color, (x, y, self.width, self.height))
            print_text(self.screen, message, y, self.height, (255, 255, 255))


def print_text(screen, message, y, height, font_color):
    font_type = pygame.font.SysFont(None, 36)
    text = font_type.render(message, True, font_color)
    screen_rect = screen.get_rect()
    x = screen_rect.centerx - text.get_width()/2
    y = y + (height - text.get_height())/2
    screen.blit(text, (x, y))

def text_height(message):
    font_type = pygame.font.SysFont(None, 36)
    text = font_type.render(message, True, (0, 0, 0))
    return text.get_height()

def text_width(message):
    font_type = pygame.font.SysFont(None, 36)
    text = font_type.render(message, True, (0, 0, 0))
    return text.get_width()
