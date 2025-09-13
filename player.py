import pygame
from settings import *
from pygame.image import load
from os.path import join

from projectile import Projectile


class Player(pygame.sprite.Sprite):

    def __init__(player, coordinates):
        super().__init__()
        player.image = load(join('graphics', 'player.png'))
        player.rect = player.image.get_rect(midbottom=coordinates)
        player.speed = 5
        player.projectile_group = pygame.sprite.Group()
        player.must_shoot = True
        player.projectile_limit = 20
        player.projectile_counter = 0

    def input(player):
        # movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            player.rect.x += player.speed

        if keys[pygame.K_LEFT]:
            player.rect.x -= player.speed
        # restrictions
        if player.rect.x >= SCREEN_WIDTH-60:
            player.rect.x = SCREEN_WIDTH-60

        if player.rect.x <= 0:
            player.rect.x = 0
        # shoot
        if keys[pygame.K_SPACE]:
            player.shoot()

    def shoot(player):
        if player.must_shoot is True:
            player.projectile_group.add(Projectile(pos=player.rect.center))
            player.must_shoot = False

    def projectile_time(player):
        if player.projectile_counter < player.projectile_limit:
            player.projectile_counter += 1
        else:
            player.projectile_counter = 0
            player.must_shoot = True

    def continuous_movement(player):
        player.projectile_group.update()

    def delete_projectile(player):
        for projectile in player.projectile_group.sprites():
            if projectile.rect.y <= 0:
                projectile.kill()

    def update(player):
        player.input()
        player.projectile_time()
        player.continuous_movement()
        player.delete_projectile()
