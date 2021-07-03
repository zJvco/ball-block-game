import pygame, sys, os

class Options:
    def __init__(self, WIDTH, HEIGHT, FPS, clock, font):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.FPS = FPS
        self.clock = clock
        self.font = font
        self.logo = pygame.transform.scale(pygame.image.load(os.path.join("assets", "logo_game_ball_block.PNG")), (self.WIDTH - 40, 200))
        self.back_button_normal = pygame.image.load(os.path.join("assets", "back_normal.PNG"))
        self.back_button_hover = pygame.image.load(os.path.join("assets", "back_hover.PNG"))
        self.credits_label = self.font.render("Created by João Victor. All rights reserved", 0, self.WHITE)

    def draw(self, WINDOW):
        WINDOW.blit(self.logo, (20, 10))
        WINDOW.blit(self.credits_label, (self.WIDTH / 2 - self.credits_label.get_width() / 2, self.HEIGHT - self.credits_label.get_height() - 10))

    def loop(self, WINDOW):
        run = True
        while run:
            WINDOW.fill(self.BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.draw(WINDOW)

            pygame.display.update()
            self.clock.tick(self.FPS)
