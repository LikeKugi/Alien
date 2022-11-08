from invasion import Invasion
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """
    bullet and its management
    """

    def __init__(self, ai_game: Invasion):
        """
        creating a bullet in the current ship's position
        :param ai_game: Invasion
        """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #  creating a bullet in (0,0) position and assignment right position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # bullet's position
        self.y = float(self.rect.y)

    def update(self):
        """
        move bullet up
        :return: None
        """
        #  renew bullet's position
        self.y -= self.settings.bullet_speed

        #  renew the rect,s position
        self.rect.y = self.y

    def draw_bullet(self):
        """
        draw a bullet on the screen
        :return: None
        """
        pygame.draw.rect(self.screen, self.color, self.rect)
