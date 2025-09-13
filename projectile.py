import pygame
from settings import *
from random import randint


class Projectile(pygame.sprite.Sprite):

    def __init__(projectile, pos):

        super().__init__()
        projectile.image = pygame.Surface((3, 15))
        projectile.image.fill('white')
        projectile.rect = projectile.image.get_rect(midbottom=pos)

    def movement(projectile):
        projectile.rect.y -= 5

    def update(projectile):
        projectile.movement()
