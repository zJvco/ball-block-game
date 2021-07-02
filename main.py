import pygame
import sys
import os
from math import sqrt
from pygame import mixer

pygame.init()

WIDTH, HEIGHT = 500, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Ball Block Game")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def main():

    def detect_collision_player(by, py):
        distance = sqrt((by - py)**2)

        if distance < ball_height:
            return True
        else:
            return False

    player_width = 120
    player_height = 10
    player_x = WIDTH / 2 - player_width / 2
    player_y = HEIGHT - player_height - 20
    player_speed = 4

    ball_width = 20
    ball_height = 20
    ball_x = WIDTH / 2 - ball_width / 2
    ball_y = player_y - 50
    ball_speed_x = 6
    ball_speed_y = 6

    #block = []
    block_width = 100
    block_height = 35

    phases = [[1, 1, 1, 1, 1],
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

    # for a in phases:
    #     for p, k in enumerate(a):
    #         print(k)

    ball_sound = mixer.Sound(os.path.join("assets", "quick_jump.wav"))

    FPS = 60

    while True:
        WINDOW.fill(BLACK)

        player = pygame.Rect(player_x, player_y, player_width, player_height)
        player_intern = pygame.Rect(
            player_x + 2, player_y + 2, player_width - 4, player_height - 4)
        ball = pygame.Rect(ball_x, ball_y, ball_width, ball_height)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and player_x <= WIDTH - player_width - 10:
            player_x += player_speed
        if keys[pygame.K_LEFT] and player_x >= 10:
            player_x -= player_speed

        pygame.draw.rect(WINDOW, WHITE, player)
        pygame.draw.rect(WINDOW, BLACK, player_intern)

        y = 0
        for i, v_row in enumerate(phases):
            x = 0
            for j, v_col in enumerate(v_row):
                if v_col == 1:
                    tile = pygame.Rect(block_width * x, block_height * y, block_width, block_height)
                    pygame.draw.rect(WINDOW, WHITE, tile, 1)

                    if ball.colliderect(tile):
                        phases[i][j] = 0
                        ball_speed_y *= -1
                x += 1
            y += 1

        if ball_y >= HEIGHT - ball_height:
            ball_x = WIDTH / 2 - ball_width / 2
            ball_y = player_y - 50
        else:
            pygame.draw.ellipse(WINDOW, WHITE, ball, 1)

        ball_x -= ball_speed_x
        ball_y -= ball_speed_y

        if ball_x <= 0 or ball_x >= WIDTH - ball_width:
            # ball_sound.play()
            ball_speed_x *= -1
        if ball_y <= 0 or ball_y >= HEIGHT - ball_height:
            # ball_sound.play()
            ball_speed_y *= -1

        if detect_collision_player(ball_y, player_y) and ball_x >= player_x and ball_x <= player_x + player_width:
            # ball_sound.play()
            ball_speed_y *= -1

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
