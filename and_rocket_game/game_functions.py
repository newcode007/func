import sys
import pygame

def check_keydown_events(event, rocket):
    """Реагирует на нажатие клавиш"""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    if event.key == pygame.K_LEFT:
        rocket.moving_left = True
    if event.key == pygame.K_UP:
        rocket.moving_up = True
    if event.key == pygame.K_DOWN:
        rocket.moving_down = True

def check_keyup_events(event, rocket):
    """Реагирует на отпускание клавищ"""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    if event.key == pygame.K_LEFT:
        rocket.moving_left = False
    if event.key == pygame.K_UP:
        rocket.moving_up = False
    if event.key == pygame.K_DOWN:
        rocket.moving_down = False

def check_events(rocket):
    """Обрабатывает нажатия клавиш и события мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, rocket)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)



def update_screen(ai_settings, screen, rocket):
    """Обновляет изображение на экране и отображает новый экран"""
    #При каждом проходе цикла перерисовывется экран
    screen.fill(ai_settings.bg_color)
    rocket.blitme()
    #Отображение последнего прорисованного экрана.
    pygame.display.flip()