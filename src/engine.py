import pymunk
import pygame
import random
from src.UI.button import Button
from src.Shape.rectangle import Rectangle
from src.Shape.circle import Circle
from src.box import Box

class Engine:
    def __init__(self):
        pygame.init();
        pygame.display.set_caption("Pymunk Physics Engine")
        self.screen = pygame.display.set_mode((1000,800))
        self.screen.fill((0,0,0))
        self.running = True
        self.space = pymunk.Space()
        self.space.gravity = 0, 1000
        self.rectlist = []
        self.circlelist = []
        Box(self.space)

    def run(self):
        while self.running:
            self.screen.fill((0,0,0))
            self.space.step(0.01)
            rectButton = Button("Rectangle", (850, 100))
            circButton = Button("Circle", (850, 400))
            for rec in self.rectlist:
                pygame.draw.rect(self.screen, (255, 255, 255), (rec.get_body().position[0] - (rec.size//2), 
                rec.get_body().position[1]-(rec.size//2), rec.size, rec.size), 0)
            for circ in self.circlelist:
                pygame.draw.circle(self.screen, (255, 255, 255), (circ.get_body().position[0],circ.get_body().position[1] ), circ.get_radius())
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if rectButton.is_clicked(pos):
                        rect = Rectangle(10, 100, (random.randint(0, 800),random.randint(200, 500)))
                        self.space.add(rect.get_body(), rect.get_shape())
                        self.rectlist.append(rect)
                    elif circButton.is_clicked(pos):
                        circ = Circle(10, 50, (random.randint(0, 800),random.randint(200, 500)))
                        self.space.add(circ.get_body(), circ.get_shape())
                        self.circlelist.append(circ)
                elif event.type == pygame.QUIT:
                    self.running = False

            rectButton.render(self.screen)
            circButton.render(self.screen)
            pygame.display.update()

        pygame.quit()

