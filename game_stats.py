

class GameStats():
    """
    Statistics for the game
    """

    def __init__(self, ai_game):
        """
        init stats
        :param ai_game: Invasion
        """
        self.settings = ai_game.settings
        self.reset_stats()
        # active state for the game
        self.game_active = False

    def reset_stats(self) -> None:
        """
        init stats, that changes during the game
        :return: None
        """
        self.ships_left = self.settings.ship_limit
