import sys
import pygame
from settings import Settings
from rocket import Rocket
import game_functions as gf

def run_game():
    # Инициализирует pygame, settings и объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_heidht))
    pygame.display.set_caption("Rocket Game")
    # Создание корабля.
    rocket = Rocket(ai_settings, screen)

    # Назначение цвета фона.
    bg_color = (230, 230, 230)

    # запуск основного цикла игры
    while True:
        gf.check_events(rocket)
        rocket.update()
        gf.update_screen(ai_settings, screen, rocket)


run_game()
