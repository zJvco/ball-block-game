import pygame, sys, os

class Menu:
    def __init__(self, WIDTH, HEIGHT, FPS, clock, font):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.FPS = FPS
        self.clock = clock
        self.logo = pygame.transform.scale(pygame.image.load(os.path.join("assets", "logo_game_ball_block.PNG")), (self.WIDTH - 40, 200))
        self.start_button_normal = pygame.transform.scale(pygame.image.load(os.path.join("assets", "start_normal.PNG")), (200, 80))
        self.start_button_hover = pygame.transform.scale(pygame.image.load(os.path.join("assets", "start_hover.PNG")), (200, 80))
        self.options_button_normal = pygame.transform.scale(pygame.image.load(os.path.join("assets", "options_normal.PNG")), (220, 80))
        self.options_button_hover = pygame.transform.scale(pygame.image.load(os.path.join("assets", "options_hover.PNG")), (220, 80))
        self.exit_button_normal = pygame.transform.scale(pygame.image.load(os.path.join("assets", "exit_normal.PNG")), (160, 80))
        self.exit_button_hover = pygame.transform.scale(pygame.image.load(os.path.join("assets", "exit_hover.PNG")), (160, 80))
        self.font = font
        self.current_button = 0
        self.credits_label = self.font.render("Created by João Victor. All rights reserved", 0, self.WHITE)
        self.stage = None

    def draw(self, WINDOW):
        WINDOW.blit(self.logo, (20, 10))

        if self.current_button == 0:
            WINDOW.blit(self.start_button_hover, (self.WIDTH / 2 - self.start_button_hover.get_width() / 2, self.HEIGHT / 2 - self.start_button_hover.get_height()))
        else:
            WINDOW.blit(self.start_button_normal, (self.WIDTH / 2 - self.start_button_normal.get_width() / 2, self.HEIGHT / 2 - self.start_button_normal.get_height()))

        if self.current_button == 1:
            WINDOW.blit(self.options_button_hover, (self.WIDTH / 2 - self.options_button_hover.get_width() / 2, self.HEIGHT / 2 - self.options_button_hover.get_height() + self.start_button_hover.get_height() + 20))
        else:
            WINDOW.blit(self.options_button_normal, (self.WIDTH / 2 - self.options_button_normal.get_width() / 2, self.HEIGHT / 2 - self.options_button_normal.get_height() + self.start_button_normal.get_height() + 20))

        if self.current_button == 2:
            WINDOW.blit(self.exit_button_hover, (self.WIDTH / 2 - self.exit_button_hover.get_width() / 2, self.HEIGHT / 2 + self.exit_button_hover.get_height() + 42))
        else:
            WINDOW.blit(self.exit_button_normal, (self.WIDTH / 2 - self.exit_button_normal.get_width() / 2, self.HEIGHT / 2 + self.exit_button_normal.get_height() + 42))

        WINDOW.blit(self.credits_label, (self.WIDTH / 2 - self.credits_label.get_width() / 2, self.HEIGHT - self.credits_label.get_height() - 10))

    def loop(self, WINDOW):
        run = True
        while run:
            WINDOW.fill(self.BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.current_button += 1
                    if event.key == pygame.K_UP:
                        self.current_button -= 1
                    if event.key == pygame.K_RETURN:
                        if self.current_button == 0:
                            self.stage = "GAME"
                            run = False
                        elif self.current_button == 1:
                            self.stage = "OPTIONS"
                            run = False
                        else:
                            pygame.quit()
                            sys.exit()

            if self.current_button > 2:
                self.current_button = 0
            elif self.current_button < 0:
                self.current_button = 2

            self.draw(WINDOW)

            pygame.display.update()
            self.clock.tick(self.FPS)
