import sys
import pygame
from settings import Settings
from ship import Ship


class Invasion:
    '''resourse management'''

    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Invasion')

        #  place ship
        self.ship = Ship(self)

        #  background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        '''main loop start'''
        while True:
            #  keyboard
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            pygame.display.flip()


if __name__ == '__main__':
    invasion = Invasion()
    invasion.run_game()
