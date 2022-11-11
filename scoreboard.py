import pygame.font



class Scoreboard:
    """
    output the game score information
    """

    def __init__(self, ai_game) -> None:
        """
        Initialise the attributes to count the score
        :param ai_game: Invasion
        """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #  font settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        #  Prepare of the image of the scoreboard
        self.prep_score()

    def prep_score(self) -> None:
        """
        modify the current score to the image
        :return: None
        """
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        #  print the score at the top of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self) -> None:
        """
        print the score
        :return: None
        """
        self.screen.blit(self.score_image, self.score_rect)
