import pymunk
import pygame
from src.UI.button import Button

class Engine:
    def __init__(self):
        pygame.init();
        pygame.display.set_caption("Pymunk Physics Engine")
        self.screen = pygame.display.set_mode((1000,1000))
        self.screen.fill((0,0,0))
        self.running = True
        self.testButton = Button("Test", (600, 200))

    def run(self):
        while self.running:
            self.testButton.render(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if self.testButton.is_clicked(pos):
                        print("Clicked!")
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.update()

        pygame.quit()

