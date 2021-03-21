import pygame

class Button:
    def __init__(self, text, topLeft):
        self.size = 100
        self.text = text
        self.topLeft = topLeft

    def render(self, surface):
        rect = pygame.Rect(self.topLeft[0], self.topLeft[1], self.size, self.size)
        pygame.draw.rect(surface, (100,100,250), rect, border_radius = 15)
        font = pygame.font.SysFont('Proxima Nova', 25, (100, 100, 200))
        text = font.render(self.text, True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = ((self.topLeft[0]+50), (self.topLeft[1])+50)
        surface.blit(text, textRect)

    def is_clicked(self, pos):
        if self.topLeft[0] <= pos[0] <= self.topLeft[0]+self.size:
            if self.topLeft[1] <= pos[1] <= self.topLeft[1]+self.size:
                return True
        return False