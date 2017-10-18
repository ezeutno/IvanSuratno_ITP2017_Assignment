import random
class Settings():
    def __init__(self):
        #Screen Settings
        self.screen_width = 500
        self.screen_height = 500
        self.bg_color = (21,41,55)

        #Ship Settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #moon Settings
        self.moon_x = int(self.screen_width * 0.15)
        self.moon_y = int(self.screen_height * 0.25)

        #Bullets Settings
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        #Star Settings
        self.percent_from_top = 1
        self.max_star = 100
        self.min_star = 50

        #Alien Settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 50
        self.fleet_direction = 1