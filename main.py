import pygame, os
from game import Game
from menu import Menu
from options import Options
from sound import Sound

class Main:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Ball Block Game")
        pygame.display.set_icon(pygame.image.load(os.path.join("assets", "icon_game_ball_block.png")))

        self.WIDTH = 500
        self.HEIGHT = 700
        self.FPS = 60
        self.WINDOW = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.font_20 = pygame.font.SysFont("comicsans", 20)
        self.font_30 = pygame.font.SysFont("comicsans", 30)
        self.screen_stage = "MENU"
        self.c_volume = 10
        self.volume = 1
        self.ball_speed = 6

    def main_loop(self):
        sound = Sound()
        sound.play_background_music()

        while True:
            if self.screen_stage == "MENU":
                menu = Menu(self.WIDTH, self.HEIGHT, self.FPS, self.clock, self.font_20)
                menu.loop(self.WINDOW)
                self.screen_stage = menu.stage
            elif self.screen_stage == "GAME":
                game = Game(self.WIDTH, self.HEIGHT, self.FPS, self.clock, sound, self.ball_speed)
                game.loop(self.WINDOW, self.WIDTH, self.HEIGHT, self.font_20)
                self.screen_stage = game.stage
            elif self.screen_stage == "OPTIONS":
                options = Options(self.WIDTH, self.HEIGHT, self.FPS, self.clock, self.font_20, self.font_30, self.c_volume, self.volume, self.ball_speed)
                options.loop(self.WINDOW, sound)
                self.c_volume = options.c_volume
                self.volume = options.volume
                self.ball_speed = options.ball_speed
                self.screen_stage = options.stage


if __name__ == "__main__":
    Main().main_loop()
