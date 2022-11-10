class Settings:
    """settings class"""

    def __init__(self) -> None:
        #  screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (137, 207, 240)

        #  the ship's moving settings
        self.ship_speed = 1

        #  bullets settings
        self.bullets_allowed = 3
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        #  aliens settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #  fleet_direction
        #       1: moving right
        #       2: moving left
        self.fleet_direction = 1
