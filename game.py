import pygame, sys
from player import Player
from ball import Ball
from tiles import Tiles
from sound import Sound

class Game:
    def __init__(self, WIDTH, HEIGHT, FPS, clock):
        self.player = Player(WIDTH, HEIGHT)
        self.ball = Ball(WIDTH, self.player.player_y)
        self.tiles = Tiles()
        self.sound = Sound()
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.FPS = FPS
        self.clock = clock
        self.stage = None

    def loop(self, WINDOW, WIDTH, HEIGHT):
        run = True
        while run:
            WINDOW.fill(self.BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.player.update()
            self.player.player_moviment(WIDTH)
            self.player.draw_player(WINDOW, self.WHITE)

            self.ball.update()
            self.ball.draw_ball(WINDOW, self.WHITE)
            self.ball.ball_moviment(WIDTH, HEIGHT, self.player.player_x, self.player.player_y, self.player.player_width, self.sound.ball_sound)

            self.tiles.draw_tiles(WINDOW, self.WHITE, self.ball, self.sound.ball_sound)

            if self.ball.ball_y >= HEIGHT - self.ball.ball_size:
                self.stage = "MENU"
                run = False

            if len(self.tiles.block) == 0:
                self.tiles.current_phase += 1

                self.ball.ball_x = WIDTH / 2 - self.ball.ball_size / 2
                self.ball.ball_y = self.player.player_y - 50

                if self.ball.ball_speed_y < 0:
                    self.ball.ball_speed_y *= -1

                if self.tiles.current_phase == 1:
                    self.tiles.phase = self.tiles.phase_1
                elif self.tiles.current_phase == 2:
                    self.tiles.phase = self.tiles.phase_2
                elif self.tiles.current_phase == 3:
                    self.tiles.phase = self.tiles.phase_3
                elif self.tiles.current_phase == 4:
                    self.tiles.phase = self.tiles.phase_4
                elif self.tiles.current_phase == 5:
                    self.tiles.phase = self.tiles.phase_5
                elif self.tiles.current_phase == 6:
                    self.tiles.phase = self.tiles.phase_6
                else:
                    self.stage = "MENU"
                    run = False

            self.tiles.clear_block_list()

            pygame.display.update()
            self.clock.tick(self.FPS)
