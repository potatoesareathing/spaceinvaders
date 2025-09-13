import pygame
from settings import *
import sys
from obstacle import Block
import obstacle
from player import Player
from alien import Alien
from random import choice, randint
from projectile import Projectile


class Game:
    def __init__(game):

        pygame.init()
        pygame.display.set_caption('Space Invaders')
        game.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        game.clock = pygame.time.Clock()
        game.player_object1 = Player(coordinates=(
            SCREEN_WIDTH - SCREEN_WIDTH/2, SCREEN_HEIGHT-20))

        game.player_group = pygame.sprite.GroupSingle()
        game.player_group.add(game.player_object1)

        game.block_size = 6
        game.shape = obstacle.shape
        game.block_group = pygame.sprite.Group()
        game.create_multiple_obstacles()
        game.alien_group = pygame.sprite.Group()
        game.create_alien()
        game.aliens = game.alien_group.sprites()
        game.alien_is_moving_right = True
        game.alien_speed = 2
        # function to add aliens at specified positions inside the group

    def create_alien(game):
        for x in range(300, 800, 50):
            for y in range(50, 400, 50):
                game.alien = Alien(choice(['yellow', 'red', 'green']), x, y)
                game.alien_group.add(game.alien)

    def create_obstacle(game, x_start, y_start):
        for row_index, row in enumerate(game.shape):
            for col_index, col in enumerate(row):
                if col == 'x':
                    x = x_start+col_index*game.block_size
                    y = y_start+row_index*game.block_size
                    game.block = Block(
                        game.block_size, color='orange', x=x, y=y)
                    game.block_group.add(game.block)
                    print(f'{game.block_group} at {x,y}')

    def create_multiple_obstacles(game, x_start=40, y_start=480):
        # creates obstacle every 150th position starting from x  = 40, y position remains the same for all, as a result, we've hardcoded y position
        for x_start in range(40, SCREEN_WIDTH, 210):
            game.create_obstacle(x_start, y_start)

    def collide_projectile(game):
        print(f'COLLIDED! {game.player_group.sprite.projectile_group}')
        pygame.sprite.groupcollide(
            game.player_group.sprite.projectile_group, game.alien_group, dokilla=True, dokillb=True)

    def alien_movement(game):

        for alien in game.aliens:

            if game.alien_is_moving_right is True:
                alien.rect.x += game.alien_speed
            else:
                alien.rect.x -= game.alien_speed

            if alien.rect.right >= SCREEN_WIDTH:
                game.alien_is_moving_right = False
                for alien in game.aliens:
                    alien.rect.y += 10

            if alien.rect.left <= 0:
                game.alien_is_moving_right = True
                for alien in game.aliens:
                    alien.rect.y += 10
# make aliens shoot

    def run(game):
        running = True

        while running:
            game.clock.tick(60)
            game.screen.fill('black')

            game.player_group.draw(game.screen)
            game.player_group.update()

            game.player_group.sprite.projectile_group.draw(game.screen)
            game.block_group.draw(game.screen)

            game.alien_group.draw(game.screen)
            game.alien_group.update()

            game.collide_projectile()
            game.alien_movement()

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
