class Settings:
    """init static game settings"""

    def __init__(self) -> None:
        #  screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (137, 207, 240)

        #  the ship's settings
        self.ship_limit = 3

        #  bullets settings
        self.bullets_allowed = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        #  aliens settings
        self.fleet_drop_speed = 10

        #  scale dynamic settings
        self.speed_up_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

        self.ship_speed = 2.0
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

    def initialize_dynamic_settings(self) -> None:
        """
        init dynamic changed settings
        :return: None
        """
        #  counter
        self.alien_points = 50

        #  speed increase factors
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0

        #  fleet_direction
        #       1: moving right
        #       2: moving left
        self.fleet_direction = 1

    def increase_speed(self) -> None:
        """
        increase speed of the game
        :return: None
        """
        self.ship_speed *= self.speed_up_scale
        self.bullet_speed *= self.speed_up_scale
        self.alien_speed *= self.speed_up_scale
        self.alien_points = int(self.alien_points * self.score_scale)
