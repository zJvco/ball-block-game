import pygame
import sys
import os
from math import sqrt

pygame.init()

WIDTH, HEIGHT = 500, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Ball Block Game")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def main():

    def detect_collision(Ay, By):
        distanceY = sqrt(((Ay - By)**2))

        if distanceY < ball_height and ball_x >= player_x and ball_x <= player_x + player_width:
            return True
        else:
            return False

    player_width = 120
    player_height = 10
    player_x = WIDTH / 2 - player_width / 2
    player_y = HEIGHT - player_height - 20
    player_speed = 5

    ball_width = 20
    ball_height = 20
    ball_x = WIDTH / 2 - ball_width / 2
    ball_y = player_y - 50
    ball_speed_x = 4
    ball_speed_y = 4

    block_img = []
    block_x = []
    block_y = []
    num_block = 50
    block_width = 50
    block_height = 35
    count_bx = 0
    count_by = 0

    FPS = 60

    while True:
        WINDOW.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and player_x <= WIDTH - player_width - 10:
            player_x += player_speed
        if keys[pygame.K_LEFT] and player_x >= 10:
            player_x -= player_speed

        pygame.draw.rect(WINDOW, WHITE, (player_x, player_y,player_width, player_height))
        pygame.draw.rect(WINDOW, BLACK, (player_x + 2,player_y + 2, player_width - 4, player_height - 4))

        for i in range(num_block):
            block_img.append(pygame.transform.scale(pygame.image.load(os.path.join("assets", "block_img.PNG")), (block_width, block_height)))
            block_x.append(count_bx)
            block_y.append(count_by)

            if block_x[i] >= WIDTH - block_width:
                count_bx = 0
                count_by += block_height
            else:
                count_bx += block_width

        for i in range(num_block):
            WINDOW.blit(block_img[i], (block_x[i], block_y[i]))

        if ball_y >= HEIGHT - ball_height:
            ball_x = WIDTH / 2 - ball_width / 2
            ball_y = player_y - 50
        else:
            pygame.draw.ellipse(WINDOW, WHITE, (ball_x, ball_y,ball_width, ball_height), 1)

        ball_x -= ball_speed_x
        ball_y -= ball_speed_y

        if ball_x <= 0 or ball_x >= WIDTH - ball_width:
            ball_speed_x *= -1
        if ball_y <= 0 or ball_y >= HEIGHT - ball_height:
            ball_speed_y *= -1

        ball_collision_player = detect_collision(ball_y, player_y)

        if ball_collision_player:
            ball_speed_y *= -1

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
