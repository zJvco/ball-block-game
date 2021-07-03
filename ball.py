import pygame
from math import sqrt

class Ball:
    def __init__(self, WIDTH, player_y):
        self.ball_size = 20
        self.ball_x = WIDTH / 2 - self.ball_size / 2
        self.ball_y = player_y - 50
        self.ball_speed_x = 10
        self.ball_speed_y = 10
        
    def update(self):
        self.ball = pygame.Rect(self.ball_x, self.ball_y, self.ball_size, self.ball_size)

    def detect_collision_player(self, by, py):
        distance = sqrt((by - py)**2)

        if distance < self.ball_size:
            return True
        else:
            return False

    def ball_moviment(self, WIDTH, HEIGHT, player_x, player_y, player_width, ball_sound):
        self.ball_x -= self.ball_speed_x
        self.ball_y -= self.ball_speed_y

        if self.ball_x <= 0 or self.ball_x >= WIDTH - self.ball_size:
            ball_sound.play()
            self.ball_speed_x *= -1
        if self.ball_y <= 0 or self.ball_y >= HEIGHT - self.ball_size:
            ball_sound.play()
            self.ball_speed_y *= -1

        if self.detect_collision_player(self.ball_y, player_y) and self.ball_x >= player_x and self.ball_x <= player_x + player_width:
            ball_sound.play()
            self.ball_speed_y *= -1

    def draw_ball(self, WINDOW, color):
        pygame.draw.ellipse(WINDOW, color, self.ball, 1)
