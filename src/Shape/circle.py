import pymunk

class Circle:
    def __init__(self, mass, radius, position):
        moment = pymunk.moment_for_circle(mass, 0, radius)
        self.body = pymunk.Body(mass, moment)
        self.body.position = position
        self.radius = radius
        self.shape = pymunk.Circle(self.body, self.radius)
        self.shape.friction = 0.3

    def get_body(self):
        return self.body

    def get_shape(self):
        return self.shape

    def get_radius(self):
        return self.radius