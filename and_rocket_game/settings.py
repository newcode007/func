class Settings():
    """Класс для хранения всех настроек игры Rocket Game"""

    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_heidht = 800
        self.bg_color = (22, 95, 243)

        # Настройки корабля
        self.rocket_speed_factor = 1.5
