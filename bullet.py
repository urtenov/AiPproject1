import pygame

class Bullet(pygame.sprite.Sprite):
    """
    Класс, который отвечает за прорисовку, появление и движение пуль
    """
    def __init__(self, screen, gun):
        """
        Принимает экран и самолет
        Создает пулю в верхней части самолета
        Задает размеры, скорость и цвет пуль
        :param screen: экран
        :param gun: самолет
        """
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.colour = 150, 211, 221
        self.speed = 10.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """
        Изменяет местоположение пули(перемещение пули вверх)
        """
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """
        Отрисовка пули на экране
        """
        pygame.draw.rect(self.screen, self.colour, self.rect)
