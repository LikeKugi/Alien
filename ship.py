import pygame


class Ship:
    """ship controls"""

    def __init__(self, ai_game) -> None:
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load image of ship
        self.image = pygame.image.load('imgs/player_ship.png')
        self.rect = self.image.get_rect()

        #  appearance of a new spaceship
        self.rect.midbottom = self.screen_rect.midbottom

        #  saving float part of moving
        self.x = float(self.rect.x)

        #  move right flag
        self.moving_right = False

        #  move left flag
        self.moving_left = False

    def update(self) -> None:
        """
        renew the ship's position in case of flag
        :return: None
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #  Update rect x coordinate
        self.rect.x = self.x

    def blitme(self) -> None:
        """paint new spaceship"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self) -> None:
        """
        place a new ship in the MIDBOTTOM
        :return: None
        """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
