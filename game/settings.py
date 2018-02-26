import os


class Settings(object):

    def __init__(self):
        """initialize the settings of game."""

        # screen settings
        self.screen_width = 960
        self.screen_height = 640
        self.screen_size = (self.screen_width, self.screen_height)
        self.bg_color = (100, 100, 100)
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.map_dir = os.path.join(self.base_dir, "img/game.tmx")
        self.max_health = 25
        self.health_color = (255, 0, 0)
        self.health_color_cover = (0, 255, 0)
        self.left_home_location = (200, 585)
        self.right_home_location = (780, 585)
        self.default_hero_num = 10


game_settings = Settings()