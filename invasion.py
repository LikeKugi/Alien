import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class Invasion:
    """resource management"""

    def __init__(self) -> None:
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
        #  init bullets
        self.bullets = pygame.sprite.Group()
        #  init aliens
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        #  background color
        self.bg_color = self.settings.bg_color

    def run_game(self) -> None:
        """main loop start"""
        while True:
            self._check_events()

            self.ship.update()
            self._update_bullets()

            self._update_screen()

            pygame.display.flip()

    def _check_events(self) -> None:
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

    def _check_keydown_events(self, event: pygame.event) -> None:
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
            #  exit
            sys.exit()
        elif event.key == pygame.K_SPACE:
            #  fire bullets
            self._fire_bullet()

    def _check_keyup_events(self, event: pygame.event) -> None:
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

    def _fire_bullet(self) -> None:
        """
        creating a new bullet and including it into the bullets group
        :return: None
        """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self) -> None:
        """
        update bullets
        :return: None
        """
        self.bullets.update()

        #  remove bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self) -> None:
        """
        creating aliens
        :return: None
        """
        alien = Alien(self)

        # calculating space between alienships and count of alienships in a row
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #  creating a row
        for alien_number in range(number_aliens_x):
            self._create_alien(alien_number)

    def _create_alien(self, alien_number: int) -> None:
        '''
        create an alien and put it in a row
        :param alien_number: int (number of alien in a row)
        :return: None
        '''
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        self.aliens.add(alien)

    def _update_screen(self) -> None:
        """
        update screen and show new screen
        :return: None
        """
        #  ship
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        #  bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        #  aliens
        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    invasion = Invasion()
    invasion.run_game()
