import pymunk

class Box:
    def __init__(self, space, p0=(0, 0), p1=(900, 700), d=4):
        x0, y0 = p0
        x1, y1 = p1
        ps = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
        for i in range(4):
            segment = pymunk.Segment(space.static_body, ps[i], ps[(i+1) % 4], d)
            segment.elasticity = 1
            segment.friction = 1
            space.add(segment)