import sys
from time import sleep
import pygame

#  import game modules
from settings import Settings
from game_stats import GameStats
from button import Button
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

        #  statistics
        self.stats = GameStats(self)

        #  place ship
        self.ship = Ship(self)
        #  init bullets
        self.bullets = pygame.sprite.Group()
        #  init aliens
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        #  create play button
        self.play_button = Button(self, 'Play')

        #  background color
        self.bg_color = self.settings.bg_color

    # ------------------------------------------------------------
    # RUN the game
    # ------------------------------------------------------------

    def run_game(self) -> None:
        """main loop start"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

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

            #  MOUSEDOWN to start the game
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

            #  KEYDOWN actions
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            #  KEYUP  actions
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    # ------------------------------------------------------------
    #  KEYBIND actions
    # ------------------------------------------------------------

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
        :return: None
        """
        if event.key == pygame.K_RIGHT:
            #  stop moving right
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            #  stop moving left
            self.ship.moving_left = False

    def _check_play_button(self, mouse_pos:pygame.event) -> None:
        """
        start the new game after the Play button pressed
        :param mouse_pos: pygame.event
            push the button
        :return: None
        """
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #  default the game stats
            self.stats.reset_stats()
            self.stats.game_active = True

            # clear the screen from alienships and bullets
            self.aliens.empty()
            self.bullets.empty()

            #  create a new fleet and a new player's ship in the midbottom
            self._create_fleet()
            self.ship.center_ship()

            #  hide the mouse while the game is active
            pygame.mouse.set_visible(False)

    # ------------------------------------------------------------
    # BULLETS actions
    # ------------------------------------------------------------

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

        #  check for collision with alienship
        #  in case of collision delete both bullet and alienship
        self._check_bullet_alien_collision()

    # ------------------------------------------------------------
    # ALIENS actions
    # ------------------------------------------------------------

    def _update_aliens(self) -> None:
        """
        update positions of alienship
        :return: None
        """
        self._check_fleet_edges()
        self.aliens.update()

        #  Check for collision with the player
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Check for collision with the bottom of the screen
        self._check_aliens_bottom()

    def _create_fleet(self) -> None:
        """
        creating aliens
        :return: None
        """
        alien = Alien(self)

        # calculating space between alienships and count of alienships in a row
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #  calculating count of rows on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        #  creating a fleet
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number: int, row_number: int) -> None:
        """
        create an alien and put it in a row
        :param alien_number: int (number of alien in a row)
        :param row_number: int (number of current row)
        :return: None
        """
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self) -> None:
        """
        reacting for reaching the edge of the screen
        :return: None
        """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self) -> None:
        """
        move the fleet down and change its direction
        :return: None
        """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1  # from fleet_direction in settings

    # ------------------------------------------------------------
    # COLLISIONS bullets, alienships and the player
    # ------------------------------------------------------------

    def _check_bullet_alien_collision(self) -> None:
        """
        treatment of bullets and alienships collisions
        :return: None
        """
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        if not self.aliens:
            #  delete current bullets and create a new fleet
            self.bullets.empty()
            self._create_fleet()

    def _check_aliens_bottom(self) -> None:
        """
        check if the alienship reaches bottom
        :return: None
        """
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # destroy the ship
                self._ship_hit()
                break

    # ------------------------------------------------------------
    # PLAYER
    # ------------------------------------------------------------

    def _ship_hit(self) -> None:
        """
        treatment of alienships and the player collisions
        :return: None
        """
        if self.stats.ships_left > 0:
            # minus ship
            self.stats.ships_left -= 1

            # clear bullets and aliens
            self.aliens.empty()
            self.bullets.empty()

            # create a new fleet and a new player's ship
            self._create_fleet()
            self.ship.center_ship()

            # pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    # ------------------------------------------------------------
    # SCREEN actions
    # ------------------------------------------------------------

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

        # show PLAY button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


# ------------------------------------------------------------
if __name__ == '__main__':
    invasion = Invasion()
    invasion.run_game()
