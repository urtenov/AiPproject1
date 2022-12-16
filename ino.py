import pygame
class Ino(pygame.sprite.Sprite):
    """
    Класс пришельца ответственен за инициализацию, вывод на экран и изменение местоположения пришельцев
    """

    def __init__(self, screen):
        """
        Инициализация и задание начальной позиции
        :param screen: экран
        """
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/pixil-frame-0 (1).png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """
        Выводит армию пришельцев на экран
        """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """
        Меняет местоположение армии пришельцев
        """
        self.y += 0.04
        self.rect.y = self.y
