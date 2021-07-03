import pygame, sys, os

class Options:
    def __init__(self, WIDTH, HEIGHT, FPS, clock, font_20, font_30, c_volume, volume, ball_speed):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.FPS = FPS
        self.clock = clock
        self.current_button = 0
        self.background = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background_image.png")), (500, 700))
        self.logo = pygame.transform.scale(pygame.image.load(os.path.join("assets", "logo_game_ball_block.PNG")), (self.WIDTH - 40, 200))
        self.back_button_normal = pygame.transform.scale(pygame.image.load(os.path.join("assets", "back_normal.PNG")), (150, 60))
        self.back_button_hover = pygame.transform.scale(pygame.image.load(os.path.join("assets", "back_hover.PNG")), (150, 60))
        self.volume_label = font_30.render("Volume:", 0, self.WHITE)
        self.volume_stick_normal = pygame.transform.scale(pygame.image.load(os.path.join("assets", "volume_stick_normal.PNG")), (10, 25))
        self.volume_stick_hover = pygame.transform.scale(pygame.image.load(os.path.join("assets", "volume_stick_hover.PNG")), (10, 25))
        self.ball_speed_label = font_30.render("Ball Speed:", 0, self.WHITE)
        self.arrow_left = pygame.transform.scale(pygame.image.load(os.path.join("assets", "arrow_left.PNG")), (30, 20))
        self.arrow_right = pygame.transform.scale(pygame.image.load(os.path.join("assets", "arrow_right.PNG")), (30, 20))
        self.enter_key = pygame.transform.scale(pygame.image.load(os.path.join("assets", "enter_key.PNG")), (30, 40))
        self.arrow_left_label = font_30.render("Move Left", 0, self.WHITE)
        self.arrow_right_label = font_30.render("Move Right", 0, self.WHITE)
        self.enter_key_label = font_30.render("Enter Menu", 0, self.WHITE)
        self.credits_label = font_20.render("Created by João Victor. All rights reserved", 0, self.WHITE)
        self.c_volume = c_volume
        self.volume = volume
        self.ball_speed = ball_speed
        self.stage = None

    def draw(self, WINDOW):
        WINDOW.blit(self.background, (0, 0))
        WINDOW.blit(self.logo, (20, 10))
        WINDOW.blit(self.arrow_left, (50, self.HEIGHT / 2 - 100))
        WINDOW.blit(self.arrow_left_label, (50 + self.arrow_left.get_width() + 10, self.HEIGHT / 2 - 100))
        WINDOW.blit(self.arrow_right, (50, self.HEIGHT / 2 - 50))
        WINDOW.blit(self.arrow_right_label, (50 + self.arrow_right.get_width() + 10, self.HEIGHT / 2 - 50))
        WINDOW.blit(self.enter_key, (50, self.HEIGHT / 2))
        WINDOW.blit(self.enter_key_label, (50 + self.enter_key.get_width() + 10, (self.HEIGHT / 2) - (self.enter_key_label.get_height() / 2) + (self.enter_key.get_height() / 2)))
        WINDOW.blit(self.volume_label, (50, self.HEIGHT / 2 + 80))

        if self.current_button == 1:
            for stick in range(self.c_volume):
                WINDOW.blit(self.volume_stick_hover, (50 * (stick / 3) + 50, self.HEIGHT / 2 + 80 + self.volume_label.get_height()))
        else:
            for stick in range(self.c_volume):
                WINDOW.blit(self.volume_stick_normal, (50 * (stick / 3) + 50, self.HEIGHT / 2 + 80 + self.volume_label.get_height()))

        WINDOW.blit(self.ball_speed_label, (self.WIDTH - self.ball_speed_label.get_width() - 100, self.HEIGHT / 2 + 80))

        if self.current_button == 2:
            for b_s in range(self.ball_speed):
                WINDOW.blit(self.volume_stick_hover, (self.WIDTH - self.ball_speed_label.get_width() - 100 + (b_s * 16), self.HEIGHT / 2 + 80 + self.volume_label.get_height()))
        else:
            for b_s in range(self.ball_speed):
                WINDOW.blit(self.volume_stick_normal, (self.WIDTH - self.ball_speed_label.get_width() - 100 + (b_s * 16), self.HEIGHT / 2 + 80 + self.volume_label.get_height()))

        if self.current_button == 0:
            WINDOW.blit(self.back_button_hover, (self.WIDTH / 2 - self.back_button_hover.get_width() / 2, self.HEIGHT - self.back_button_hover.get_height() - 100))
        else:
            WINDOW.blit(self.back_button_normal, (self.WIDTH / 2 - self.back_button_normal.get_width() / 2, self.HEIGHT - self.back_button_normal.get_height() - 100))

        WINDOW.blit(self.credits_label, (self.WIDTH / 2 - self.credits_label.get_width() / 2, self.HEIGHT - self.credits_label.get_height() - 10))

    def loop(self, WINDOW, sound):
        run = True
        while run:
            WINDOW.fill(self.BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.current_button += 1
                    if event.key == pygame.K_DOWN:
                        self.current_button -= 1

                    if self.current_button == 1:
                        if event.key == pygame.K_LEFT:
                            self.c_volume -= 1
                            self.volume -= 0.1
                        if event.key == pygame.K_RIGHT:
                            self.c_volume += 1
                            self.volume += 0.1

                    if self.current_button == 2:
                        if event.key == pygame.K_LEFT:
                            self.ball_speed -= 1
                        if event.key == pygame.K_RIGHT:
                            self.ball_speed += 1

                    if event.key == pygame.K_RETURN:
                        if self.current_button == 0:
                            self.stage = "MENU"
                            run = False

            if self.current_button > 2:
                self.current_button = 0
            elif self.current_button < 0:
                self.current_button = 2

            if self.c_volume > 10:
                self.c_volume = 10
            elif self.c_volume < 0:
                self.c_volume = 0

            if self.volume > 1:
                self.volume = 1
            elif self.volume < 0:
                self.volume = 0

            if self.ball_speed > 10:
                self.ball_speed = 10
            elif self.ball_speed < 0:
                self.ball_speed = 0

            self.draw(WINDOW)
            sound.volume_control(self.volume)

            pygame.display.update()
            self.clock.tick(self.FPS)
