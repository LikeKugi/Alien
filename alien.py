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
        self.settings = ai_game.settings

        #  load alien's image and set rect attribute
        self.image = pygame.image.load('imgs/alien_ship.png')
        self.rect = self.image.get_rect()

        #  appearence a new alienship TOPLEFT
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #  saving horizontal position af an alienship
        self.x = float(self.rect.x)

    def check_edges(self) -> bool:
        """
        check if the alienship is close to the edge
        :return: bool
            True - if next to the edge
        """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self) -> None:
        """
        move alien to the right or to the left
        :return: None
        """
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
