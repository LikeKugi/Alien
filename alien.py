import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """
    single alien ship
    """

    def __init__(self, ai_game):
        """
        initialize alien spaceship and it's position
        :param ai_game: Invasion
        """
        super().__init__()
        self.screen = ai_game.screen

        #  load alien's image and set rect attribute
        self.image = pygame.image.load('imgs/alien_ship.png')
        self.rect = self.image.get_rect()

        #  appearence a new alienship TOPLEFT
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #  saving horizontal position af an alienship
        self.x = float(self.rect.x)
