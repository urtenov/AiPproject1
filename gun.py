import pygame
from pygame.sprite import Sprite
class Gun(Sprite):
    """
    логика самолета
    """
    def __init__(self, screen):
        """
        Функция инициализирует самолет
        Принимает экран
        :param screen: получаем экран
        :param image: загружаем изображение самолета
        :param rect: представляем в виде прямоугольника самолет
        :param screen_rect: представляем в виде прямоугольника экран
        :param rect.centerx: центр самолета
        :param rect.bottom: низ самолета
        :param mright: хранит значение False чтобы при запуске игры самолет сразу не начал движение вправо
        :param mleft: хранит значение False чтобы при запуске игры самолет сразу не начал движение влево
        """
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/pixil-frame-0.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        """функция, которая отрисовывает самолет"""
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """
        Обновление позиции самолета.
        Ограничение движения самолета, чтобы он не вышел за пределы окна в момент движения.

        """
        if self.mright and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        elif self.mleft and self.rect.left > 0:
            self.rect.centerx -= 1


    def create_gun(self):
        """
        Создание самолета
        """
        self.center = self.screen_rect.centerx

