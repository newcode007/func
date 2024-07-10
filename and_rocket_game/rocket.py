import pygame
class Rocket():
    def __init__(self,ai_settings,screen):
        """Инициализирует ракету и задает его начальную позицию."""
        self.screen = screen
        self.ai_settings = ai_settings

        #Загрузка изображения корабля и получение прямоугольника.
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Каждый новый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


        # Сохранение вещественной координаты центра корабля.
        self.center = float(self.rect.centerx)

        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def update(self):
        """Обновляет позицию ракеты с учетом флагов"""
        """Обнуляется атрибут center, не rect."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.rocket_speed_factor
        if self.moving_left and self.rect.left > 0 :
            self.center -= self.ai_settings.rocket_speed_factor
        #if self.moving_up and self.rect.update() < self.screen_rect.update:
         #   self.y += self.ai_settings.rocket_speed_factor
        #if self.moving_down and self.rect.down > 0 :
         #   self.y -= self.ai_settings.rocket_speed_factor
        #Обновление атрибута rect на основании self.senter
        self.rect.centerx = self.center



    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)