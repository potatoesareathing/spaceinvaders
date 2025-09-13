import pygame
from pygame.image import load
import os
from settings import *
from projectile import Projectile
from random import randint


class Alien(pygame.sprite.Sprite):

    def __init__(alien, color, x, y):

        super().__init__()
        alien.image = load(os.path.join('graphics', f'{color}.png'))
        alien.rect = alien.image.get_rect(topleft=(x, y))
        alien.projectile_group = pygame.sprite.Group()
