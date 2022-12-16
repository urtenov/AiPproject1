from unittest import TestCase
import pygame
from gun import Gun
import controls
from pygame.sprite import Group
from stats import Stats
from scores import Scores
from ino import Ino
from bullet import Bullet

class Test(TestCase):
    def test_update_bullets(self):

        pygame.init()
        screen = pygame.display.set_mode((700, 800), flags=pygame.HIDDEN)
        gun = Gun(screen)
        bullets = Group()
        inos = Group()
        stats = Stats()
        scor = Scores(screen, stats)
        gun.rect.x = 10
        gun.rect.y = 10
        ino = Ino(screen)

        inos.add(ino)

        new_bullet = Bullet(screen, gun)
        new_bullet.rect.y = 12
        new_bullet.rect.x = 12
        new_bullet.speed = 0
        bullets.add(new_bullet)
        # new_bullet.x = 100
        bg_colour = (4, 50, 70)
        controls.update(bg_colour, screen, stats, scor, gun, inos, bullets)
        ino.rect.x = 10
        ino.rect.y = 10
        controls.update_bullets(screen, stats, scor, inos, bullets)
        self.assertEqual(0, len(bullets))

