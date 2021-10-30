import grid
import random

class SideWinder:
    def __init__(self, g):
        for row in g.grid:
            run = []
            for c in row:
                run.append(c)
                if c.north == None and c.east == None:
                    continue
                if c.north == None or (random.randrange(2) == 0 and not c.east == None):
                    c.link(c.east)
                else:
                    up = random.choice(run)
                    up.link(up.north)
                    run = []
