import pygame
import sys
from bullet import Bullet
from ino import Ino
import time

def events(screen, gun, bullets):
    """
    Обрабатывает события
    Принимает объект экрана, самолет и пули.
    При нажатии на крестик в углу экрана выходит из игры;
    При нажатии на стрелку Право самолет движется вправо;
    При нажатии на стрелку Влево самолет движется влево
    При нажатии на Пробел создается пуля
    :param screen: экран
    :param gun: самолет
    :param bullets: пули
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                gun.mright = True
            elif event.key == pygame.K_LEFT:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                gun.mright = False
            elif event.key == pygame.K_LEFT:
                gun.mleft = False
def update(bg_colour, screen, stats, scor, gun, ino,  bullets):
    """
    Обновляет экран
    Принимает фоновый цвет экрана, объект экрана, статистические данные, объект самолет, объект группы пришельцев, объекты пуль
    :param bg_colour: цвет фона
    :param screen: экран
    :param stats: статистика
    :param scor: счет
    :param gun: самолет
    :param ino: пришельцы
    :param bullets: пули
    """
    screen.fill(bg_colour)
    scor.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    ino.draw(screen)
    pygame.display.flip()

def update_bullets(screen, stats, scor, inos, bullets):
    """
    Обновляет позиции пуль и счет и армию пришельцев: если пуля улетает за пределы окна она уничтожается; если пуля уничтожает пришельца, то добавляет очки в статистику; если все пришельцы уничтожены, то создает новых пришельцев
    :param screen: экран
    :param stats: статистика
    :param scor: счет
    :param inos: пришельцы
    :param bullets: пули
    """
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
    if collisions:
        for inos in collisions.values():
            stats.score += 10 * len(inos)
        scor.image_score()
        scor.image_guns()
    if len(inos) == 0:
        bullets.empty()
        create_army(screen, inos)

def create_army(screen, inos):
    """
    Создает армию пришельцев
    :param screen: экран
    :param inos: пришельцы
    """
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((700-2 * ino_width)/ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((700-2*ino_height)/ino_height)

    for row_number in range(number_ino_y - 16):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + ino_width * ino_number
            ino.y = ino_height + ino_height * row_number + 60
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + ino.rect.height * row_number
            inos.add(ino)

def update_inos(stats, screen, scor, gun, inos, bullets):
    """
    Обновляет позиции пришельцев, проверяет столкнулись ли самолет и пришельцы
    :param stats: статистика
    :param screen: экран
    :param scor: счет
    :param gun: самолет
    :param inos: пришельцы
    :param bullets: пули
    """
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gun_kill(stats, screen, scor, gun, inos, bullets)
    inos_check(stats, screen, scor, gun, inos, bullets)


def gun_kill(stats, screen, scor, gun, inos, bullets):
    """
    Обрабатывает столкновение самолета и пришельца. Уничтожает самолет и вычитает жизнь
    :param stats: статистика
    :param screen: экран
    :param scor: счет
    :param gun: самолет
    :param inos: пришельцы
    :param bullets: пули
    """

    if stats.guns_left > 1:
        stats.guns_left -= 1
        scor.image_guns()
        inos.empty()
        bullets.empty()
        create_army(screen, inos)
        gun.create_gun()
        time.sleep(2)
    else:
        stats.run_game = False
        sys.exit()

def inos_check(stats, screen, scor, gun, inos, bullets):
    """
    Проверяет прошли ли пришельцы самолет
    :param stats: статистика
    :param screen: экран
    :param scor: счет
    :param gun: самолет
    :param inos: пришельцы
    :param bullets: пули
    """
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, scor, gun, inos, bullets)
            break
