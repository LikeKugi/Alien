import pygame


class Ship:
    '''ship controls'''

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load image of ship
        self.image = pygame.image.load('imgs/player_ship.png')
        self.rect = self.image.get_rect()

        #  appearance of a new spaceship
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        '''paint new spaceship'''
        self.screen.blit(self.image, self.rect)
