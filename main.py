import pygame, os
from game import Game
from menu import Menu
from options import Options

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
        self.font = pygame.font.SysFont("comicsans", 20)
        self.screen_stage = "MENU"

    def main_loop(self):
        while True:
            if self.screen_stage == "MENU":
                menu = Menu(self.WIDTH, self.HEIGHT, self.FPS, self.clock, self.font)
                menu.loop(self.WINDOW)
                self.screen_stage = menu.stage
            elif self.screen_stage == "GAME":
                game = Game(self.WIDTH, self.HEIGHT, self.FPS, self.clock)
                game.loop(self.WINDOW, self.WIDTH, self.HEIGHT)
                self.screen_stage = game.stage
            elif self.screen_stage == "OPTIONS":
                options = Options(self.WIDTH, self.HEIGHT, self.FPS, self.clock, self.font)
                options.loop(self.WINDOW)


if __name__ == "__main__":
    Main().main_loop()
