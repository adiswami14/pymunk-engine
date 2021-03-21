import pymunk
from pymunk import Vec2d

class Rectangle:
    def __init__(self, mass, size, position):
        self.size = size
        moment = pymunk.moment_for_box(mass, (self.size, self.size))
        self.body = pymunk.Body(mass, moment)
        self.body.position = position
        self.shape = pymunk.Poly.create_box(self.body, (self.size, self.size))
        self.shape.friction = 0.3
        self.shape.color = (1, 0, 0, 1)

    def get_body(self):
        return self.body

    def get_shape(self):
        return self.shape