import pygame

class Player:
    def __init__(self, WIDTH, HEIGHT):
        self.player_width = 120
        self.player_height = 10
        self.player_x = WIDTH / 2 - self.player_width / 2
        self.player_y = HEIGHT - self.player_height - 20
        self.player_speed = 5

    def update(self):
        self.player = pygame.Rect(self.player_x, self.player_y, self.player_width, self.player_height)

    def player_moviment(self, WIDTH):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.player_x <= WIDTH - self.player_width - 10:
            self.player_x += self.player_speed
        if keys[pygame.K_LEFT] and self.player_x >= 10:
            self.player_x -= self.player_speed

    def draw_player(self, WINDOW, color):
        pygame.draw.rect(WINDOW, color, self.player, 1)
