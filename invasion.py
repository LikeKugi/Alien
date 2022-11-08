import sys
import pygame
from settings import Settings
from ship import Ship


class Invasion:
    """resource management"""

    def __init__(self):
        pygame.init()

        self.settings = Settings()

        #  screen settings  |  start option - window_mode
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        #  title
        pygame.display.set_caption('Invasion')

        #  place ship
        self.ship = Ship(self)

        #  background color
        self.bg_color = self.settings.bg_color

    def run_game(self):
        """main loop start"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

            pygame.display.flip()

    def _check_events(self):
        """
        check ivents or key mapped
        :return: None
        """
        #  keyboard
        for event in pygame.event.get():

            #  exit game
            if event.type == pygame.QUIT:
                sys.exit()

            #  KEYDOWN actions
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            #  KEYUP  actions
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """
        reaction for keydown
        :param event: pygame.event
        :return: None
        """
        if event.key == pygame.K_RIGHT:
            #  move right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            #  move left
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """
        reaction for keyup
        :param event: pygame.event
        :return:
        """
        if event.key == pygame.K_RIGHT:
            #  stop moving right
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            #  stop moving left
            self.ship.moving_left = False

    def _update_screen(self):
        """
        update screen and show new screen
        :return: None
        """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()


if __name__ == '__main__':
    invasion = Invasion()
    invasion.run_game()
