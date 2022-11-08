class Settings:
    """settings class"""

    def __init__(self):
        #  screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (137, 207, 240)

        #  the ship's moving settings
        self.ship_speed = 1

        #  bullets settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
