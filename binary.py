import grid
import random

class BinaryTree:
    def __init__(self, g):
        for c in g.cells():
            # build north and east candidates
            n = []
            if not c.north == None:
                n.append(c.north)
            if not c.east == None:
                n.append(c.east)

            # choose a random candidate
            if len(n) > 0:
                chosen = random.choice(n)
                c.link(chosen)


