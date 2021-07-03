import pygame

class Tiles:
    def __init__(self):
        self.block = []
        self.block_width = 100
        self.block_height = 35
        self.tile = None
        self.current_phase = 1
        self.phase_1 = [[1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0]]
        self.phase_2 = [[1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1],
                        [0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0],
                        [1, 0, 0, 0, 1],
                        [0, 1, 1, 1, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0]]
        self.phase_3 = [[0, 0, 1, 0, 0],
                        [0, 1, 1, 1, 0],
                        [1, 1, 0, 1, 1],
                        [1, 1, 1, 1, 1],
                        [0, 1, 1, 1, 0],
                        [0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 1, 1, 1, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0]]
        self.phase_4 = [[1, 1, 1, 1, 1],
                        [0, 1, 0, 1, 0],
                        [0, 1, 1, 1, 0],
                        [1, 0, 1, 0, 1],
                        [1, 0, 1, 0, 1],
                        [1, 1, 1, 1, 1],
                        [0, 0, 0, 0, 0],
                        [0, 1, 1, 1, 0],
                        [0, 0, 0, 0, 0],
                        [0, 1, 1, 1, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0]]
        self.phase_5 = [[1, 1, 1, 1, 1],
                        [1, 0, 0, 0, 1],
                        [1, 0, 1, 0, 1],
                        [1, 0, 1, 0, 1],
                        [1, 0, 0, 0, 1],
                        [1, 1, 1, 1, 1],
                        [1, 1, 0, 1, 1],
                        [0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0]]
        self.phase_6 = [[1, 0, 1, 0, 1],
                        [0, 1, 0, 1, 0],
                        [1, 0, 1, 0, 1],
                        [0, 1, 0, 1, 0],
                        [1, 0, 1, 0, 1],
                        [0, 1, 0, 1, 0],
                        [0, 0, 1, 0, 0],
                        [1, 0, 0, 0, 1],
                        [0, 1, 1, 1, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0]]
        self.phase = self.phase_1

    def update(self, x, y):
        self.tile = pygame.Rect(self.block_width * x, self.block_height * y, self.block_width, self.block_height)

    def clear_block_list(self):
        self.block.clear()

    def draw_tiles(self, WINDOW, color, ball, ball_sound):
        y = 0
        for i, v_row in enumerate(self.phase):
            x = 0
            for j, v_col in enumerate(v_row):
                if v_col == 1:
                    self.update(x, y)
                    pygame.draw.rect(WINDOW, color, self.tile, 1)

                    self.block.append(pygame.Rect(self.block_width * x, self.block_height * y, self.block_width, self.block_height))

                    if ball.ball.colliderect(self.tile):
                        ball_sound.play()
                        self.phase[i][j] = 0
                        self.block.pop()
                        ball.ball_speed_y *= -1
                x += 1
            y += 1
