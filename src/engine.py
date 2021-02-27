import pymunk
import pygame

class Engine:
    def __init__(self):
        pygame.init();
        pygame.display.set_caption("Pymunk Physics Engine")
        self.screen = pygame.display.set_mode((500,500))
        self.screen.fill((0,0,0))
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.update()

        pygame.quit()

